
import tensorflow as tf

new_model = tf.keras.models.load_model('imdb_classifier.model')

def predictor(message):
    prediction = list(new_model.predict(message))
    prediction[0][0] *= 100
    prediction = round(prediction[0][0],2)
    if prediction < 40:
        state = "Negative"
    elif prediction >= 40 and prediction < 60:
        state = "Neutral"
    else:
        state = "Positive"
    prediction = str(prediction) + "% >>> " + state + " review."
    return prediction

predictor(["An amazing movie i loved it so much. The scene with the llamas was a bit strange though. Didn't like the lead male actor i have to admit"])


# raw_test_ds = tf.keras.utils.text_dataset_from_directory(
#      'aclImdb/test', 
#      batch_size=32)

# # loss, accuracy = new_model.evaluate(raw_test_ds)
# # print(accuracy)

# examples = [
#     "Super movie, one of the best i've seen although i didn't like the scene with the crocodiles",
#     "The movie was good...",
#     "The movie was terrible...",
#     "I thought it was the best movie I've ever seen!",
#     "This was the greatest movie ever written. I hope they make a sequel, so brill i want to see more",
  
# ]


# predict_list = list(new_model.predict(examples))

# for i in range(len(examples)):
#     print(round(predict_list[i][0],4))

# for i in range(len(examples)):
#     predict_list[i][0] = round(predict_list[i][0],4)


# def review_checker(input_examples, input_data):
#     for i in range(len(input_examples)):
#         if input_data[i][0] < 0.4:
#             review = "Negative"
#         elif input_data[i][0] >= 0.4 and input_data[i][0] < 0.6:
#             review = "Neutral"
#         elif input_data[i][0] >= 0.6:
#             review = "Positive"
#         print(input_examples[i] , " " , input_data[i][0], " >>> ", review)
#         # results = [input_data[i][0], " >>> ", review]
#         # return results


# review_checker(examples, predict_list)



# #  
# example_input = [input("Enter your review here")]


# prediction_input = new_model.predict(list(example_input))

# print(prediction_input)
# review_checker(example_input, prediction_input)