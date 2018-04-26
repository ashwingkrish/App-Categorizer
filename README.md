# App-Categorizer

This project is used to determine the type of app, based on only the description. There are currently 5 categories that can be detected:
* Communication
* Travel
* Files
* Food
* Productivity

It uses Sci-kit Learn's SGDClassifier and CountVectorizer to perform the classification.

The data being used by the SGDClassifier is obtained from AppData.csv. The data had been compiled and pickled previously into appdata2.pickle.
The notebook ```count_classifier.ipynb``` illustrates the actual training and testing of the the SGDClassifier. 

With the data, it has an accuracy of 94.44%

If you wish to directly use the classifier without viewing the learning, use the ```categorizer.py``` file. Once you input the text, press Enter again.

Examples:

```
python3 categorizer.py
Enter the app description:
with Evernote, organizing your tasks becomes easier than ever.

App is categorized as: Productivity
```

```
Enter the app description:
Join WhatsApp and get in touch with your friends and family with end to end encryption!

App is categorized as: Communication
```

```
Enter the app description:
Book cheap flights and train tickets

App is categorized as: Travel
```

This project works very well with any description from the Google Play Store