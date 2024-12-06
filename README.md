DIC PROJECT TEAM 19

PROBLEM STATEMENT -  Chemical impact evaluation to identify beneficial and harmful ingredients for skin care products

TEAM MEMBERS:

Anirudh Nadig - 50613184 anadig2@buffalo.edu

Satya Vaishnavi Jami - 50592365 Satyavai@buffalo.edu

Rachana Dharmavaram - 50604169 rachanad@buffalo.edu

---------------------------------------------------------PHASE 2 -------------------------------------------------------

HYPOTHESIS 1 - Does the popularity or status of a product depend on variables other than price? - ANIRUDH NADIG 50613184

CODE START - CELL 249
ANALYSIS - AFTER CELL 258

HYPOTHESIS 2 - Are particular chemical categories more common in makeup products compared to others? RACHANA DHARMAVARAM 50604169

CODE START - CELL 259
ANALYSIS - AFTER CELL 268

HYPOTHESIS 3 - Hypothesis 3: Most of the toxic heavy chemicals are still in use --> ANIRUDH NADIG 50613184

CODE START - CELL 271
ANALYSIS - BEFORE CELL 271 ,272, 273

HYPOTHESIS 4 - Is there a relationship among a product’s popularity or consumer rating and the amount of compounds with few destructive outcomes? - Satya vaishnavi Jami 50592365

CODE START - CELL 275
ANALYSIS - AFTER CELL 285

HYPOTHESIS 5 - Do clients price products with color-adding chemical substances decrease or better than the ones without them? - Satya vaishnavi Jami 50592365

CODE START - CELL 286
ANALYSIS - AFTER CELL 286

Hypothesis 6- Are products designed for certain skin kind like sensitive skin, much more likely to pass over potentially harmful chemicals? - RACHANA DHARMAVARAM 50604169

CODE START - CELL 287
ANALYSIS - BEFORE CELL 287,288 / AFTER CELL 291

src/ contains all ipynb code , pdf file with output, cosmetics dataset, chemicals-in-cosmetics dataset, merged-data dataset & README file

################################################### PHASE 3 ###############################################################################################

DIC PROJECT PHASE 3 RUNNING THE CODE ON LOCAL MACHINE:-

1) clone the GitHub repo

2) Run the "database_setup.py" to create a sqllite3 database for storage

3) Run the "app.py" file to run flask

4) Try to have extensions such as "live server" and "sqllite viewer" on vscode for easier use

5) Now click on the app.html file OR in vscode right click on app.html -> click on "open with live server" . This prompts open a new page

6) Enter the prompts as you see fit. Data will be displayed

7) Go back to the "recommendations.db" and click to see the data being stored


*) It is also possible to upload the code on a container and try to get it on online but containers costs money to store . Also to combat CORS some steps need to be taken to make sure we dont get the 405 http errors. I would recommend fly.io for such operations

*)Have also tested the responses on postman and it works as intended with the POST and GET calls working. For POST we need to give the body and content type as application/json