# LoanWay

LoanWay is an API for a machine learning model that predicts from some data supplied by the user how eligible they are for a loan.

# How to get started

You can clone the project directly from github by running `git clone https://github.com/Olamidun/LoanWay.git` or by downloading the zip file, run `pip install -r requirements.txt` to install the necessary dependencies and then `python manage.py runserver` to fire up the server. Do not forget to migrate your models by running `python manage.py makemigrations` and `python manage.py migrate`.


# Documentation
The API has four endpoints:
* The login endpoint (localhost:8000/api/auth/login) which takes in request in this form:
 ````json
  {
    "username": "admin",
    "password": "admin"
  }
 ````
 
 Response returned by this endpoint:
 ```json
 {
    "token": "c0f10bb374113d19943ee4f4ceff37fcfe147217"
 }
 ````
 
 * The check eligibility endpoint (localhost:8000/api/apply)
 The endpoint accepts only post request with the body in this format:
 ```javascript
   {  
      "First_name": "<first_name>",
      "Last_name": "<last_name>",
      "Email": "<email>",
      "Dependents": <integer>,
      "ApplicantIncome": <integer>,
      "CoapplicantIncome": <integer>,
      "LoanAmount": <float>,
      "Loan_Amount_Term": <integer>,
      "Credit_History": <integer>,
      "Married": "Yes",
      "Gender": "Male",
      "Education": "Graduate",
      "Self_Employed": "Yes",
      "Property_Area": "Urban"
   }
 ```
 
 Married and the Self_Employed parameters taks in either "Yes" or "No" as its value. The first letter of either "Yes" or "No" must be in capital.
 Gender takes in either "*Male*" or "*Female*" with the first letter of the value being passed in Capital.
 Education parameter takes in "*Graduate*" or "*Not Graduate*", with the first letter of the value being passed in also in capital.
 Property_Area parameter takes in either "*Urban*", "*Semiurban*", "*Rural*" as its parameter. Like the previous parameters, first letter of the value being passed in must be in capital.
 
 Response returned by this endpoint:
 ```javascript
 {
    "id": 63,
    "user": 1, //user id
    "First_name": "Kolapo",
    "Last_name": "Olamidun",
    "Email": "kolaloloolamidun@gmail.com",
    "Dependents": 0,
    "ApplicantIncome": 25000,
    "CoapplicantIncome": 10000,
    "LoanAmount": 2008.0,
    "Loan_Amount_Term": 360,
    "Credit_History": 1,
    "Gender": "Male",
    "Married": "Yes",
    "Education": "Graduate",
    "Self_Employed": "Yes",
    "Property_Area": "Urban",
    "date_applied": "2021-08-31T19:21:28.740590Z",
    "eligible_for_loan": true // prediction gotten from the machine learning model based on the request.       If user is eligible for loan, it returns true, else it returns false
}
 ```
 
 This endpoint requires token authentication, to authenticate, you add `Authorization: Token <token_value>` to your headers.
 
* The next endpoint is the list applied loans endpoint (localhost:8000/api/your_applications) which accepts GET requests. This endpoint also requires token authentication and it is done as exlained above.
* The response returned by this endpoint is a list of all the loan eligibility done by the logged in user:
  ```json
  [
    {
        "id": 56,
        "user": 1,
        "First_name": "Kolapo",
        "Last_name": "Olamidun",
        "Email": "ooolamidun@gmail.com",
        "Dependents": 0,
        "ApplicantIncome": 100,
        "CoapplicantIncome": 500,
        "LoanAmount": 78.0,
        "Loan_Amount_Term": 360,
        "Credit_History": 1,
        "Gender": "Male",
        "Married": "Yes",
        "Education": "Graduate",
        "Self_Employed": "Yes",
        "Property_Area": "Rural",
        "date_applied": "2021-08-31T18:23:53.592609Z",
        "eligible_for_loan": false
    },
    {
        "id": 58,
        "user": 1,
        "First_name": "Kolapo",
        "Last_name": "Olamidun",
        "Email": "kolapooolamidun@gmail.com",
        "Dependents": 0,
        "ApplicantIncome": 10000,
        "CoapplicantIncome": 60000,
        "LoanAmount": 78.0,
        "Loan_Amount_Term": 360,
        "Credit_History": 1,
        "Gender": "Male",
        "Married": "Yes",
        "Education": "Graduate",
        "Self_Employed": "Yes",
        "Property_Area": "Urban",
        "date_applied": "2021-08-31T18:43:59.912257Z",
        "eligible_for_loan": false
    },
    {
        "id": 59,
        "user": 1,
        "First_name": "Kolapo",
        "Last_name": "Olamidun",
        "Email": "kolapioolamidun@gmail.com",
        "Dependents": 0,
        "ApplicantIncome": 5000,
        "CoapplicantIncome": 400,
        "LoanAmount": 2008.0,
        "Loan_Amount_Term": 360,
        "Credit_History": 1,
        "Gender": "Male",
        "Married": "Yes",
        "Education": "Graduate",
        "Self_Employed": "Yes",
        "Property_Area": "Urban",
        "date_applied": "2021-08-31T18:44:27.325118Z",
        "eligible_for_loan": false
    },
    {
        "id": 60,
        "user": 1,
        "First_name": "Kolapo",
        "Last_name": "Olamidun",
        "Email": "kolapioloolamidun@gmail.com",
        "Dependents": 0,
        "ApplicantIncome": 25000,
        "CoapplicantIncome": 10000,
        "LoanAmount": 2008.0,
        "Loan_Amount_Term": 360,
        "Credit_History": 1,
        "Gender": "Male",
        "Married": "Yes",
        "Education": "Graduate",
        "Self_Employed": "Yes",
        "Property_Area": "Urban",
        "date_applied": "2021-08-31T18:44:59.694937Z",
        "eligible_for_loan": false
    },
    {
        "id": 61,
        "user": 1,
        "First_name": "Kolapo",
        "Last_name": "Olamidun",
        "Email": "kolapeoloolamidun@gmail.com",
        "Dependents": 0,
        "ApplicantIncome": 25000,
        "CoapplicantIncome": 10000,
        "LoanAmount": 2008.0,
        "Loan_Amount_Term": 360,
        "Credit_History": 1,
        "Gender": "Male",
        "Married": "Yes",
        "Education": "Graduate",
        "Self_Employed": "Yes",
        "Property_Area": "Urban",
        "date_applied": "2021-08-31T18:49:24.568041Z",
        "eligible_for_loan": true
    }
  ]
  ```
If a user hasn't checked for their eligibility to apply for loan, the endpoint returns an empty list.
  
  
  * The last endpoint (localhost:8000/api/your_application/<id>) accepts GET requests, it is for       retrieving a single loan eligibility details.
  This endpoint also requires token authentication and it return a response like this:
  ```json
   {
    "id": 56,
    "user": 1,
    "First_name": "Kolapo",
    "Last_name": "Olamidun",
    "Email": "ooolamidun@gmail.com",
    "Dependents": 0,
    "ApplicantIncome": 100,
    "CoapplicantIncome": 500,
    "LoanAmount": 78.0,
    "Loan_Amount_Term": 360,
    "Credit_History": 1,
    "Gender": "Male",
    "Married": "Yes",
    "Education": "Graduate",
    "Self_Employed": "Yes",
    "Property_Area": "Rural",
    "date_applied": "2021-08-31T18:23:53.592609Z",
    "eligible_for_loan": false
  }
  ```
  If an id which does not exist is passed into the url, it returns a 404 error saying 
 ```json
  {
    "detail": "Not found."
  }
 ```