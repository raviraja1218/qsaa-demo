import hashlib
gemma_text = "Gemma predicts: AI rules!"
mock_cipher = hashlib.sha256(gemma_text.encode()).hexdigest()
print("Mock ‘Kyber’ on ‘Gemma’:", mock_cipher)