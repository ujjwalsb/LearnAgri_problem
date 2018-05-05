Model the following data:


-> Farmer data > Phone number, Name, Language
-> Farm data > Area, Village, Crop grown, Sowing date
-> Schedule data > Days after sowing, Fertiliser, Quantity, Quantity unit(ton, kg, g
    for solids and L, mL for liquids)

Views needed
-> Find all schedules due for today / tomorrow
-> Find all farmers who are growing a crop
-> Given prices of fertilisers, calculate the bill of materials for a single farmer

Note:
There is a 'sowing date' parameter in farm which defines when sowing was done.
A farm will have multiple schedules and they have a parameter called 'days from sowing'
which define how many days the schedule is followed after sowing.
We want to know when a schedule is due, given by 'sowing date' + 'days from sowing'

-----------------------------------------------------------------------------------------

Steps:

    1. cd LearnArgri_problem
    2. source venv/bin/activate
    3. pip install -r requirements.txt
    4. cd farmer
    5. python manage.py runserver
    6. open - http://127.0.0.1:8000

* There are no data in the database, all the entries is to be filled.
