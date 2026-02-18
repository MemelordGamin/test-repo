"""
StrictCode — FastAPI Endpoint Test Suite

Tests the /scan and /health endpoints using FastAPI's TestClient.
Validates request validation, scan responses, and error handling.
"""

import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from fastapi.testclient import TestClient
from api.main import app


client = TestClient(app)


# ===================================================================
# FIXTURES
# ===================================================================

CLEAN_CODE = '''
def process_data(data):
    """Process incoming data safely."""
    try:
        result = data.strip()
        return result
    except ValueError as e:
        raise RuntimeError(f"Failed: {e}") from e
'''

BAD_CODE = '''
def bad_function(x):
    try:
        return x + 1
    except Exception:
        pass

import fast_api_secure_plugin
'''


# ===================================================================
# TESTS
# ===================================================================

def test_root_endpoint():
    """GET / should return API info."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "StrictCode"
    print("  ✅ test_root_endpoint")


def test_health_endpoint():
    """GET /health should return system status."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "version" in data
    assert "podman_available" in data
    assert "image_exists" in data
    print(f"  ✅ test_health_endpoint (status={data['status']})")


def test_scan_clean_code_passes():
    """POST /scan with clean code should return PASS."""
    response = client.post("/scan", json={"code": CLEAN_CODE})
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "pass", f"Expected 'pass', got '{data['status']}'"
    assert data["findings_count"] == 0
    assert "duration_ms" in data
    print(f"  ✅ test_scan_clean_code_passes ({data['duration_ms']:.0f}ms)")


def test_scan_bad_code_fails():
    """POST /scan with bad code should return FAIL with findings."""
    response = client.post("/scan", json={"code": BAD_CODE})
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "fail"
    assert data["findings_count"] >= 3

    rule_ids = {f["rule_id"] for f in data["findings"]}
    assert "AST001" in rule_ids, "Should detect missing docstring"
    assert "AST004" in rule_ids, "Should detect except:pass"
    assert "DEP001" in rule_ids, "Should detect hallucinated import"
    print(f"  ✅ test_scan_bad_code_fails ({data['duration_ms']:.0f}ms)")


def test_scan_empty_code_rejected():
    """POST /scan with empty/whitespace code should return 422."""
    response = client.post("/scan", json={"code": "   "})
    assert response.status_code == 422
    print("  ✅ test_scan_empty_code_rejected")


def test_scan_missing_code_rejected():
    """POST /scan without code field should return 422."""
    response = client.post("/scan", json={"language": "python"})
    assert response.status_code == 422
    print("  ✅ test_scan_missing_code_rejected")


def test_scan_unsupported_language():
    """POST /scan with unsupported language should return 422."""
    response = client.post("/scan", json={
        "code": "console.log('hello')",
        "language": "javascript",
    })
    assert response.status_code == 422
    print("  ✅ test_scan_unsupported_language")


def test_scan_response_structure():
    """Response JSON should have the expected structure."""
    response = client.post("/scan", json={"code": CLEAN_CODE})
    data = response.json()

    required_keys = {"status", "findings", "findings_count", "metrics", "metadata"}
    assert required_keys.issubset(data.keys()), (
        f"Missing keys: {required_keys - data.keys()}"
    )
    print("  ✅ test_scan_response_structure")


def test_process_time_header():
    """X-Process-Time header should be present on all responses."""
    response = client.get("/health")
    assert "x-process-time" in response.headers, "Missing X-Process-Time header"
    print("  ✅ test_process_time_header")


def test_scan_findings_severity():
    """Findings should have valid severity values."""
    response = client.post("/scan", json={"code": BAD_CODE})
    data = response.json()
    valid_severities = {"low", "medium", "high", "critical"}
    for finding in data["findings"]:
        assert finding["severity"] in valid_severities, (
            f"Invalid severity: {finding['severity']}"
        )
    print("  ✅ test_scan_findings_severity")


# ===================================================================
# RUNNER
# ===================================================================

def run_all_tests():
    """Run all API tests."""
    tests = [
        test_root_endpoint,
        test_health_endpoint,
        test_scan_clean_code_passes,
        test_scan_bad_code_fails,
        test_scan_empty_code_rejected,
        test_scan_missing_code_rejected,
        test_scan_unsupported_language,
        test_scan_response_structure,
        test_process_time_header,
        test_scan_findings_severity,
    ]

    print("=" * 60)
    print("  StrictCode — FastAPI Endpoint Tests")
    print("=" * 60)
    print()

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"  ❌ {test.__name__}: {e}")
            failed += 1
        except Exception as e:
            print(f"  💥 {test.__name__}: CRASH — {type(e).__name__}: {e}")
            failed += 1

    print()
    print("-" * 60)
    print(f"  Results: {passed} passed, {failed} failed, {passed + failed} total")
    print("-" * 60)

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(run_all_tests())
