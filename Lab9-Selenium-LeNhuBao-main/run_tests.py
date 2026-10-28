import os
import sys
import pytest


def main():
    print("=" * 60)
    print("  SELENIUM AUTOMATED TESTING SUITE - SAUCEDEMO (SWAG LABS)")
    print("  Student: Nguyen Xuan Tu")
    print("  ID: 23010538")
    print("=" * 60)

    # Ensure directories exist
    os.makedirs("screenshots", exist_ok=True)
    os.makedirs("reports", exist_ok=True)

    # Run pytest with HTML report
    pytest_args = [
        "tests",
        "-v",
        "--html=reports/report.html",
        "--self-contained-html"
    ]

    print("\n[+] Running test suite with pytest...")
    exit_code = pytest.main(pytest_args)

    print("\n" + "=" * 60)
    if exit_code == 0:
        print("  ALL TEST CASES PASSED SUCCESSFULLY! (8/8)")
    else:
        print(f"  Tests finished with exit code: {exit_code}")
    print(f"  Screenshots saved to: {os.path.abspath('screenshots')}")
    print(f"  HTML Report saved to: {os.path.abspath('reports/report.html')}")
    print("=" * 60)

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
