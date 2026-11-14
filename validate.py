#!/usr/bin/env python3
"""
Automated Verification & Evaluation Script for FIoT Laboratory Submission
Student: Venkataprabu V (25011102114)
Course: Foundations of IoT (FIoT) Lab
"""

import os
import re
import sys
import glob
import base64

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))

# ANSI Colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

# 8051 Tasks and expected artifacts
TASKS_8051 = [
    ("8051/CAT2/TASK2A", ["bringup.c", "STARTUP.A51", "*.uvproj", "Objects/*.hex", "README.md", "circuit.png"]),
    ("8051/CAT2/TASK2B", ["blink.c", "STARTUP.A51", "*.uvproj", "Objects/*.hex", "README.md", "circuit.png"]),
    ("8051/CAT2/TASK2C", ["controller.c", "STARTUP.A51", "*.uvproj", "Objects/*.hex", "README.md", "circuit.png"]),
    ("8051/CAT3/TASK3A", ["lab3.c", "STARTUP.A51", "*.uvproj", "Objects/*.hex", "README.md", "circuit.png"]),
    ("8051/CAT4/TASK4A", ["lab4.c", "STARTUP.A51", "*.uvproj", "Objects/*.hex", "README.md", "circuit.png"]),
    ("8051/CAT5/TASK5A", ["fade.c", "STARTUP.A51", "*.uvproj", "Objects/*.hex", "README.md", "circuit.png"]),
    ("8051/CAT5/TASK5B", [
        "README.md", "circuit.png",
        "TASK5B.1/square_wave.c", "TASK5B.1/STARTUP.A51", "TASK5B.1/*.uvproj", "TASK5B.1/Objects/*.hex",
        "TASK5B.2/square_wave.c", "TASK5B.2/STARTUP.A51", "TASK5B.2/*.uvproj", "TASK5B.2/Objects/*.hex",
        "TASK5B.3/square_wave.c", "TASK5B.3/STARTUP.A51", "TASK5B.3/*.uvproj", "TASK5B.3/Objects/*.hex"
    ]),
    ("8051/CAT5/TASK5C", ["stepper.c", "STARTUP.A51", "*.uvproj", "Objects/*.hex", "README.md", "circuit.png"]),
    ("8051/CAT6/TASK6A", ["uart_tx.c", "STARTUP.A51", "*.uvproj", "Objects/*.hex", "README.md", "circuit.png"]),
    ("8051/CAT6/TASK6B", ["lab6.c", "STARTUP.A51", "*.uvproj", "Objects/*.hex", "README.md", "circuit.png"]),
    ("8051/CAT7/TASK7A", ["lcd_both_rows.c", "STARTUP.A51", "*.uvproj", "Objects/*.hex", "README.md", "circuit.png"]),
    ("8051/CAT7/TASK7B", ["lcd_update.c", "STARTUP.A51", "*.uvproj", "Objects/*.hex", "README.md", "circuit.png"]),
    ("8051/CAT7/TASK7C", ["lcd_move.c", "STARTUP.A51", "*.uvproj", "Objects/*.hex", "README.md", "circuit.png"]),
]

# STM32 Tasks and expected artifacts
STM32_COMMON = [
    "README.md", "circuit.png", "*.ioc", ".mxproject",
    "Core", "Drivers", "MDK-ARM/*.uvprojx", "MDK-ARM/startup_*.s"
]

TASKS_STM32 = [
    ("STM32/CAT8/TASK8A", STM32_COMMON),
    ("STM32/CAT8/TASK8B", STM32_COMMON),
    ("STM32/CAT8/TASK8C", STM32_COMMON),
    ("STM32/CAT9/TASK9A", STM32_COMMON),
    ("STM32/CAT9/TASK9B", STM32_COMMON),
    ("STM32/CAT10/TASK10A", STM32_COMMON),
    ("STM32/CAT10/TASK10B", STM32_COMMON),
    ("STM32/CAT10/TASK10C", STM32_COMMON),
    ("STM32/CAT11/TASK11A", STM32_COMMON),
    ("STM32/CAT12/TASK12A", STM32_COMMON),
    ("STM32/CAT12/TASK12B", STM32_COMMON),
    ("STM32/CAT12/TASK12C", STM32_COMMON),
    ("STM32/CAT13/TASK13A", STM32_COMMON),
    ("STM32/CAT13/TASK13B", STM32_COMMON),
    ("STM32/CAT13/TASK13C", STM32_COMMON),
    ("STM32/CAT14/TASK14", STM32_COMMON),
    ("STM32/CAT15/TASK15", STM32_COMMON + ["flows-recengine.json"]),
]

CAT_SUMMARIES = [
    "8051/CAT2/README.md",
    "8051/CAT3/README.md",
    "8051/CAT4/README.md",
    "8051/CAT5/README.md",
    "8051/CAT6/README.md",
    "8051/CAT7/README.md",
    "STM32/CAT8/README.md",
    "STM32/CAT9/README.md",
    "STM32/CAT10/README.md",
    "STM32/CAT11/README.md",
    "STM32/CAT12/README.md",
    "STM32/CAT13/README.md",
    "STM32/CAT14/README.md",
    "STM32/CAT15/README.md",
]

# Obfuscated banned strings so this validation script doesn't trigger false positives
_B64_TARGETS = [
    "ZWluY29zbW9z",          # eincosmos
    "MjUwMTExMDIxMTc=",      # 25011102117
    "dmlzaHdh",              # vishwa
    "ZGV2ZWluY29zbW9z"       # deveincosmos
]
FORBIDDEN_IDENTIFIERS = [base64.b64decode(b).decode("utf-8") for b in _B64_TARGETS]


def check_pattern(base_dir, pattern):
    full_pattern = os.path.join(base_dir, pattern)
    matches = glob.glob(full_pattern)
    return len(matches) > 0


def validate_tasks():
    results = []
    all_passed = True

    print(f"\n{BOLD}{CYAN}=== 1. TASK ARTIFACT VERIFICATION ==={RESET}")
    print(f"{'Task Identifier':<24} | {'Status':<8} | {'Missing Artifacts / Details'}")
    print("-" * 75)

    all_tasks = TASKS_8051 + TASKS_STM32
    for rel_path, req_patterns in all_tasks:
        task_dir = os.path.join(REPO_ROOT, rel_path)
        missing = []

        if not os.path.isdir(task_dir):
            missing.append("DIRECTORY MISSING")
        else:
            for pat in req_patterns:
                if not check_pattern(task_dir, pat):
                    missing.append(pat)

        status = "PASS" if not missing else "FAIL"
        if status == "FAIL":
            all_passed = False
            status_str = f"{RED}{BOLD}FAIL{RESET}"
            detail = f"{RED}{', '.join(missing)}{RESET}"
        else:
            status_str = f"{GREEN}{BOLD}PASS{RESET}"
            detail = "All required files present"

        print(f"{rel_path:<24} | {status_str:<17} | {detail}")
        results.append((rel_path, status, missing))

    return all_passed


def validate_cat_summaries():
    print(f"\n{BOLD}{CYAN}=== 2. CAT SUMMARY README VERIFICATION ==={RESET}")
    all_passed = True
    for cat_readme in CAT_SUMMARIES:
        full_path = os.path.join(REPO_ROOT, cat_readme)
        exists = os.path.isfile(full_path)
        if exists:
            print(f"{cat_readme:<30} | {GREEN}{BOLD}PASS{RESET}")
        else:
            print(f"{cat_readme:<30} | {RED}{BOLD}FAIL (MISSING){RESET}")
            all_passed = False
    return all_passed


def validate_root_readme_links():
    print(f"\n{BOLD}{CYAN}=== 3. ROOT README.MD RELATIVE LINK CHECK ==={RESET}")
    readme_path = os.path.join(REPO_ROOT, "README.md")
    if not os.path.isfile(readme_path):
        print(f"{RED}Root README.md is missing!{RESET}")
        return False

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
    broken_links = []
    valid_links = 0

    for label, target in links:
        if target.startswith("http://") or target.startswith("https://") or target.startswith("#"):
            continue
        target_path = target.split("#")[0].strip()
        if not target_path:
            continue
        full_target = os.path.normpath(os.path.join(REPO_ROOT, target_path))
        if not (os.path.isfile(full_target) or os.path.isdir(full_target)):
            broken_links.append((label, target))
        else:
            valid_links += 1

    if broken_links:
        print(f"{RED}Found {len(broken_links)} broken relative links in README.md:{RESET}")
        for label, target in broken_links:
            print(f"  - [{label}] -> {target}")
        return False
    else:
        print(f"{GREEN}{BOLD}PASS:{RESET} All {valid_links} relative documentation links verified successfully.")
        return True


def validate_sanitization():
    print(f"\n{BOLD}{CYAN}=== 4. IDENTIFIER SANITIZATION (ZERO-TOLERANCE CHECK) ==={RESET}")
    found_violations = []

    for root, dirs, files in os.walk(REPO_ROOT):
        if ".git" in dirs:
            dirs.remove(".git")
        for f in files:
            file_path = os.path.join(root, f)
            rel_path = os.path.relpath(file_path, REPO_ROOT)
            
            # Skip validate.py itself
            if os.path.abspath(file_path) == os.path.abspath(__file__):
                continue

            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as fh:
                    text = fh.read().lower()
                    for identifier in FORBIDDEN_IDENTIFIERS:
                        if identifier in text:
                            found_violations.append((rel_path, identifier))
            except Exception:
                pass

    if found_violations:
        print(f"{RED}{BOLD}FAIL:{RESET} Found {len(found_violations)} occurrences of forbidden identifiers:")
        for rel_p, iden in found_violations:
            print(f"  - {rel_p}: contains '{iden}'")
        return False
    else:
        print(f"{GREEN}{BOLD}PASS:{RESET} Zero forbidden identifiers found across entire repository.")
        return True


def main():
    print(f"\n{BOLD}======================================================================{RESET}")
    print(f"{BOLD}         FIoT LABORATORY SUBMISSION AUTOMATED EVALUATOR               {RESET}")
    print(f"{BOLD}         Candidate: Venkataprabu V | Reg: 25011102114                  {RESET}")
    print(f"{BOLD}======================================================================{RESET}")

    t_pass = validate_tasks()
    c_pass = validate_cat_summaries()
    l_pass = validate_root_readme_links()
    s_pass = validate_sanitization()

    print(f"\n{BOLD}======================================================================{RESET}")
    print(f"{BOLD}                         EVALUATION SUMMARY                           {RESET}")
    print(f"{BOLD}======================================================================{RESET}")
    print(f"Task Project Files & Schematics: {'PASS' if t_pass else 'FAIL'}")
    print(f"CAT Summary Documents:           {'PASS' if c_pass else 'FAIL'}")
    print(f"Documentation Hyperlinks:        {'PASS' if l_pass else 'FAIL'}")
    print(f"Identity Sanitization Check:     {'PASS' if s_pass else 'FAIL'}")
    print(f"----------------------------------------------------------------------")

    if t_pass and c_pass and l_pass and s_pass:
        print(f"{GREEN}{BOLD}OVERALL VERDICT: ALL TESTS PASSED (100% READY FOR SUBMISSION){RESET}\n")
        return 0
    else:
        print(f"{RED}{BOLD}OVERALL VERDICT: SOME CHECKS FAILED - PLEASE REVIEW ABOVE{RESET}\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
