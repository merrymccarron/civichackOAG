-- SQL Functions supplied by Kevin.Ryan@ag.ny.gov on 26 May 2015 13:57

CREATE OR REPLACE PACKAGE Nyu_Funcs IS

     FUNCTION Translate_Contract_Type(p_Contract_Type IN VARCHAR2)
          RETURN VARCHAR2;
     FUNCTION Translate_Contrib_Code_Type(p_Contrib_Code_Type IN VARCHAR2)
          RETURN VARCHAR2;

     FUNCTION Translate_Contribution_Code(p_Contribution_Code IN VARCHAR2)
          RETURN VARCHAR2;
     FUNCTION Translate_Freport(p_Freport IN VARCHAR2) RETURN VARCHAR2;

     FUNCTION Translate_Transaction_Code(p_Transaction_Code IN VARCHAR2)
          RETURN VARCHAR2;

     FUNCTION Translate_State(p_State IN VARCHAR2) RETURN VARCHAR2;

END Nyu_Funcs;
/
CREATE OR REPLACE PACKAGE BODY Nyu_Funcs IS

     Gv_Replace_Text VARCHAR2(10) := 'N/A';

     FUNCTION Translate_Contract_Type(p_Contract_Type IN VARCHAR2)
          RETURN VARCHAR2 AS
          v_Translation VARCHAR2(200);
     BEGIN
          SELECT CASE
                      WHEN (p_Contract_Type = 'B') THEN
                       ('Minority')
                      WHEN (p_Contract_Type = 'L') THEN
                       ('Municipality (water, sewer, fire districts)')
                      WHEN (p_Contract_Type = 'M') THEN
                       ('Municipality (county, city, town, village, school district, community college)')
                      WHEN (p_Contract_Type = 'N') THEN
                       ('Not-For-Profit Organization')
                      WHEN (p_Contract_Type = 'S') THEN
                       ('Small Business')
                      WHEN (p_Contract_Type = 'W') THEN
                       ('Women Owned')
                      WHEN (p_Contract_Type = 'X') THEN
                       ('All Others')
                      ELSE
                       'All Others'
                 END AS "contract_code"
          INTO   v_Translation
          FROM   Dual;
          RETURN v_Translation;
     END Translate_Contract_Type;

     FUNCTION Translate_Contrib_Code_Type(p_Contrib_Code_Type IN VARCHAR2)
          RETURN VARCHAR2 AS
          v_Translation VARCHAR2(200);
     BEGIN
          SELECT CASE
                      WHEN (p_Contrib_Code_Type = '1') THEN
                       ('Services/Facilities Provided')
                      WHEN (p_Contrib_Code_Type = '2') THEN
                       ('Property Given')
                      WHEN (p_Contrib_Code_Type = '3') THEN
                       ('Campaign Expenses Paid')
                      ELSE
                       Gv_Replace_Text
                 END AS "contrib_type_code_25"
          INTO   v_Translation
          FROM   Dual;
          RETURN v_Translation;
     END Translate_Contrib_Code_Type;

     FUNCTION Translate_Contribution_Code(p_Contribution_Code IN VARCHAR2)
          RETURN VARCHAR2 AS
          v_Translation VARCHAR2(500);
     BEGIN
          SELECT CASE
                      WHEN (p_Contribution_Code = 'CAN') THEN
                       ('Candidate/Candidate Spouse')
                      WHEN (p_Contribution_Code = 'FAM') THEN
                       ('Family Members')
                      WHEN (p_Contribution_Code = 'CORP') THEN
                       ('Corporate')
                      WHEN (p_Contribution_Code = 'IND') THEN
                       ('Individual')
                      WHEN (p_Contribution_Code = 'PART') THEN
                       ('Partnership')
                      WHEN (p_Contribution_Code = 'COM') THEN
                       ('Committee')
                      ELSE
                       Gv_Replace_Text
                 END AS "contrib_code_20"
          INTO   v_Translation
          FROM   Dual;
          RETURN v_Translation;
     END Translate_Contribution_Code;
     FUNCTION Translate_Freport(p_Freport IN VARCHAR2) RETURN VARCHAR2 AS
          v_Translation VARCHAR2(200);
     BEGIN
          SELECT CASE
                      WHEN (p_Freport = 'A') THEN
                       ('32 Day Pre Primary')
                      WHEN (p_Freport = 'B') THEN
                       ('11 Day Pre Primary')
                      WHEN (p_Freport = 'C') THEN
                       ('10 Day Post Primary')
                      WHEN (p_Freport = 'D') THEN
                       ('32 Day Pre General')
                      WHEN (p_Freport = 'E') THEN
                       ('11 Day Pre General')
                      WHEN (p_Freport = 'F') THEN
                       ('27 Day Post General')
                      WHEN (p_Freport = 'G') THEN
                       ('32 Day Pre Special')
                      WHEN (p_Freport = 'H') THEN
                       ('11 Day Pre Special')
                      WHEN (p_Freport = 'I') THEN
                       ('27 Day Post Special')
                      WHEN (p_Freport = 'J') THEN
                       ('Periodic Jan.')
                      WHEN (p_Freport = 'K') THEN
                       ('Periodic July')
                      WHEN (p_Freport = 'L') THEN
                       ('24 hour Notice')
                      ELSE
                       Gv_Replace_Text
                 END AS "freport_id"
          INTO   v_Translation
          FROM   Dual;
          RETURN v_Translation;
     END Translate_Freport;

     FUNCTION Translate_Transaction_Code(p_Transaction_Code IN VARCHAR2)
          RETURN VARCHAR2 AS
          v_Translation VARCHAR2(200);
     BEGIN
          SELECT CASE
                       WHEN (p_Transaction_Code = 'A') THEN
                        ('Monetary Contributions/Individual and Partnerships')
                       WHEN (p_Transaction_Code = 'B') THEN
                        ('Monetary Contributions/Corporate')
                       WHEN (p_Transaction_Code = 'C') THEN
                        ('Monetary Contributions/All Other')
                       WHEN (p_Transaction_Code = 'D') THEN
                        ('In-Kind Contributions')
                       WHEN (p_Transaction_Code = 'E') THEN
                        ('Other Receipts')
                       WHEN (p_Transaction_Code = 'F') THEN
                        ('Expenditure/Payments')
                       WHEN (p_Transaction_Code = 'G') THEN
                        ('Transfers In')
                       WHEN (p_Transaction_Code = 'H') THEN
                        ('Transfers Out')
                       WHEN (p_Transaction_Code = 'I') THEN
                        ('Loans Received')
                       WHEN (p_Transaction_Code = 'J') THEN
                        ('Loan Repayments')
                       WHEN (p_Transaction_Code = 'K') THEN
                        ('Liabilities/Loans Forgiven')
                       WHEN (p_Transaction_Code = 'L') THEN
                        ('Expenditure Refunds')
                       WHEN (p_Transaction_Code = 'M') THEN
                        ('Contributions Refunded')
                       WHEN (p_Transaction_Code = 'N') THEN
                        ('Outstanding Liabilities')
                       WHEN (p_Transaction_Code = 'O') THEN
                        ('Partners / Subcontracts')
                       WHEN (p_Transaction_Code = 'P') THEN
                        ('Non Campaign Housekeeping Receipts')
                       WHEN (p_Transaction_Code = 'Q') THEN
                        ('Non Campaign Housekeeping Expenses')
                       WHEN (p_Transaction_Code = 'R') THEN
                        ('Allocated Expenses (Aggregate party expenses on specific candidates. These are not specific expenses. Please see the resources section for

further information.')
                       ELSE
                        Gv_Replace_Text
                  END AS "transaction_code"
          INTO   v_Translation
          FROM   Dual;
          RETURN v_Translation;
     END Translate_Transaction_Code;

     FUNCTION Translate_State(p_State IN VARCHAR2) RETURN VARCHAR2 AS
          v_Translation VARCHAR2(30);
          v_State       VARCHAR2(30);
     BEGIN
          v_State := TRIM(Upper(p_State));
          SELECT CASE
                      WHEN (v_State = 'AL') THEN
                       ('Alabama')
                      WHEN (v_State = 'AK') THEN
                       ('Alaska')
                      WHEN (v_State = 'AZ') THEN
                       ('Arizona')
                      WHEN (v_State = 'AR') THEN
                       ('Arkansas')
                      WHEN (v_State = 'CA') THEN
                       ('California')
                      WHEN (v_State = 'CO') THEN
                       ('Colorado')
                      WHEN (v_State = 'CT') THEN
                       ('Connecticut')
                      WHEN (v_State = 'DE') THEN
                       ('Delaware')
                      WHEN (v_State = 'FL') THEN
                       ('Florida')
                      WHEN (v_State = 'GA') THEN
                       ('Georgia')
                      WHEN (v_State = 'HI') THEN
                       ('Hawaii')
                      WHEN (v_State = 'ID') THEN
                       ('Idaho')
                      WHEN (v_State = 'IL') THEN
                       ('Illinois')
                      WHEN (v_State = 'IN') THEN
                       ('Indiana')
                      WHEN (v_State = 'IA') THEN
                       ('Iowa')
                      WHEN (v_State = 'KS') THEN
                       ('Kansas')
                      WHEN (v_State = 'KY') THEN
                       ('Kentucky')
                      WHEN (v_State = 'LA') THEN
                       ('Louisiana')
                      WHEN (v_State = 'ME') THEN
                       ('Maine')
                      WHEN (v_State = 'MD') THEN
                       ('Maryland')
                      WHEN (v_State = 'MA') THEN
                       ('Massachusetts')
                      WHEN (v_State = 'MI') THEN
                       ('Michigan')
                      WHEN (v_State = 'MN') THEN
                       ('Minnesota')
                      WHEN (v_State = 'MS') THEN
                       ('Mississippi')
                      WHEN (v_State = 'MO') THEN
                       ('Missouri')
                      WHEN (v_State = 'MT') THEN
                       ('Montana')
                      WHEN (v_State = 'NE') THEN
                       ('Nebraska')
                      WHEN (v_State = 'NV') THEN
                       ('Nevada')
                      WHEN (v_State = 'NH') THEN
                       ('New Hampshire')
                      WHEN (v_State = 'NJ') THEN
                       ('New Jersey')
                      WHEN (v_State = 'NM') THEN
                       ('New Mexico')
                      WHEN (v_State = 'NY') THEN
                       ('New York')
                      WHEN (v_State = 'NC') THEN
                       ('North Carolina')
                      WHEN (v_State = 'ND') THEN
                       ('North Dakota')
                      WHEN (v_State = 'OH') THEN
                       ('Ohio')
                      WHEN (v_State = 'OK') THEN
                       ('Oklahoma')
                      WHEN (v_State = 'OR') THEN
                       ('Oregon')
                      WHEN (v_State = 'PA') THEN
                       ('Pennsylvania')
                      WHEN (v_State = 'RI') THEN
                       ('Rhode Island')
                      WHEN (v_State = 'SC') THEN
                       ('South Carolina')
                      WHEN (v_State = 'SD') THEN
                       ('South Dakota')
                      WHEN (v_State = 'TN') THEN
                       ('Tennessee')
                      WHEN (v_State = 'TX') THEN
                       ('Texas')
                      WHEN (v_State = 'UT') THEN
                       ('Utah')
                      WHEN (v_State = 'VT') THEN
                       ('Vermont')
                      WHEN (v_State = 'VA') THEN
                       ('Virginia')
                      WHEN (v_State = 'WA') THEN
                       ('Washington')
                      WHEN (v_State = 'WV') THEN
                       ('West Virginia')
                      WHEN (v_State = 'WI') THEN
                       ('Wisconsin')
                      WHEN (v_State = 'WY') THEN
                       ('Wyoming')
                      ELSE
                       p_State
                 END AS "state"
          INTO   v_Translation
          FROM   Dual;
          RETURN v_Translation;
     END Translate_State;

END Nyu_Funcs;
/
