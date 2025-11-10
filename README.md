My makeup project looks at the millions of dollars traded in beef and veal across the United States from 2000 to 2024. The beef industry is a significant part of the U.S. economy, influencing agricultural practices, trade policies, and consumer behavior. Understanding the patterns in beef trading can provide insights into economic trends, regional production strengths, and market demands. The goal of this dashboard is to illustrate the trends of beef & veal trading with interactive visualizations that can be filtered by yearly or state trends. I learned that having multiple forms of filters, buttons, visualizations, and trends demonstrate data in a fun and knowledgable way. 

The audience may include economists, farmers, meat producers, distributors and supply chain managers who want to look at trends state-by-state for the beef market in order to make data-driven decisions.

The value of the Dash App lies within the interactive map with the slider that allows the user to look at trends over time and hovering over states to see the values and the changes that take place. Also, the line graph page that shows the difference in trade values over time is useful because you can select the specific state you want to look at with the dropdown menu at the top of the page. These interactive visualizations and filters allow the user to find exactly what they're looking for.

How to Run
Locally:
- Use this link to open the github site that contains all files https://github.com/ampiercy/CTBA_FINAL
- cd CTBA
- pip install -r requirements.txt
- Run finalproject.py file
- Click on the link in the terminal of the Dash app. It should be similar to http://127.0.0.1:8050/

How to Run
Via Render:
- Uploaded all files created into github repo
- Went to Render and create a new web service
- Linked the CTBA_Final_Project repo
- Chose Python 3 Environment, pip install
- Build Command: pip install -r requirements.txt
- Start Command: gunicorn finalproject:app
- Selected deploy
- Website was created along with this link: https://ctba-final.onrender.com

Data Sources: 
The beef_trading.csv was accessed via the USDA Economic Research Service. The link to the website for the downloadable data is https://www.ers.usda.gov/data-products/state-agricultural-trade-data . I specifically looked for data that was separated by state and year so I could create filters and look at data based on year and have an effective interactive map of the US with data on every state. The spreadsheet initially had data on more than just beef and veal trading, but I deleted all of the other data and kept only the beef and veal information. 

Data Dictionary:
In the beef_trading.csv There are five different columns containing different data. Commodity, which states the product traded. In the case of the dash, I only used the Beef and veal data and deleted all other data. State, which shows each state in the US and repeats for every year. Units, which shows the amount sold in units which is "Million Dollars". Year, which contains the years 2000-2023 for each state. Value, which is the amount of money traded by state. The value is in millions of dollars. 