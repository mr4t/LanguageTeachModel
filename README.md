# LanguageTeachModel
learn language about profession

## Requirements
install the requirement modules from requirements.txt 
set your mysql database and make your changes from new_database.py between lines 12-21

## How To Use

sign_in_screen.py is main file to use app. After run file you can train new model about your profession with using pdf sources or websites and you can learn from your saved model.

### Train
For train the model you got 2 selection : PDF - WEBSİTE
### -PDF
For train the model from pdf change pdf menu and give exact pdf path
### -WEBSİTE
i used web scapping for train the model from websites
in any website have an hieararchy for example our website is https://www.language.com/ . And this website using "topic" name in url for categories and using "article" name for news

select website from app and give homepage and write the category(it will seen on sign_in_screen for learn from this table later)
for topic line if you write just "topic" app will scrape all website or just scrape about your proffession(for example write topic/technology sure it sould be in website hierarchy)
and write article line "article" 

after you gave this informations click start. First program will take all usable urls, after will scrape all article urls, words taken from this pages will go some process and finally words will save to mysql database
(If your ui will stop while training ignore it, when train is done in big text area will shown COMPLETED info. just wait until see this)

### Learn
just select saved table you want to learn and click learn.
you will see google translate website in qt web browser engine and there three button to control back-delete-next


