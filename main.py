from model import predict_feedback

feedback = input("Enter student feedback: ")
result = predict_feedback(feedback)

print("Predicted Sentiment:", result)

