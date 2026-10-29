# Test Samples — Phishing URL Awareness Checker

## Testing Environment

- Language: Python
- Python version: Python 3.14.8
- Operating system: Windows
- Code editor: Visual Studio Code

## Test Cases

### Test 1: Normal Example URL

**Input:** `https://www.example.com/login`

**Expected:** No listed warning signs found.

**Actual:** No listed warning signs found. The program reminded the user that this does not prove the URL is safe.

**Status:** PASS

### Test 2: IP Address and HTTP

**Input:** `http://192.0.2.10/account`

**Expected:** IP address hostname warning and HTTP warning.

**Actual:** Both expected warnings were displayed.

**Status:** PASS

### Test 3: URL Contains an @ Symbol

**Input:** `http://example.com@sample.invalid/login`

**Expected:** @ symbol warning and HTTP warning.

**Actual:** Both expected warnings were displayed.

**Status:** PASS

### Test 4: Many Hostname Segments

**Input:** `https://a.b.c.d.e.example.invalid/path`

**Expected:** Hostname segments warning.

**Actual:** The warning about many dot-separated hostname segments was displayed.

**Status:** PASS

### Test 5: Punycode Hostname

**Input:** `https://xn--example.invalid/`

**Expected:** Punycode warning.

**Actual:** The warning about a punycode label was displayed.

**Status:** PASS

## Additional Improvement Tests

- Multiple URLs can be checked in the same program session without restarting it.
- The `quit` command exits the program.
- Warning messages explain the detected patterns in plain language.

## Testing Notes

The program checks URL text only. It does not visit websites, scan for malware, or prove that a URL is safe. All test inputs are examples used for educational purposes.
