from hello import get_message

def test_hello_default_message():
    """Verify that hello.py returns expected message with default parameters."""
    result = get_message("MLOps")
    print(f"\n[TEST LOG] Output message: {result}")
    assert "Hello, MLOps!" in result
    assert "Welcome to MLOps UAT Environment." in result
