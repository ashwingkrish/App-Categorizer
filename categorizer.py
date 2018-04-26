import pickle
import warnings

# load the SGDClassifier from the pickle
with open('sgd_classifier.pickle', 'rb') as f:
	text_clf_svm = pickle.load(f)

print("Enter the app description:")

lines = []

# take multiple lines as input till the input is empty
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = ['\n'.join(lines)]

categories = ['Communication',
    'Travel',
    'Files',
    'Food',
    'Productivity']

# ignore warnings
with warnings.catch_warnings():
	warnings.simplefilter("ignore")
	# predict the category of the app
	c = text_clf_svm.predict(text)
print("App is categorized as: ", categories[c[0]])