import pymysql
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

connection = pymysql.connect(
  host = "gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
  port = 4000,
  user = "7DkLfiMgGiBGjAQ.root",
  password = "HintC73CrUxoLeb3",
  database = "trialdb",
  ssl_verify_cert = True,
  ssl_verify_identity = True,
  
  
)
mycursor=connection.cursor()



#### Q-1
mycursor.execute("""Select product_id,sum(sale_price*quantity) as Revenue from trialdb.project_trial_2
                 group by product_id
                 order by revenue desc
                 limit 10""")
out=mycursor.fetchall()
q_1=pd.DataFrame(out,columns=['Product_id','Revenue'])


### Q-2

mycursor.execute("""Select e.city,sum(d.profit) as Profit_Margin
                 from trialdb.project_trial e
                 inner join project_trial_2 d on e.order_id=d.order_id
                 group by e.city
                 order by Profit_Margin desc
                 limit 5""")
out=mycursor.fetchall()
q_2=pd.DataFrame(out,columns=['City','Profit_Margin'])

### Q-3
mycursor.execute("""Select e.category,sum(d.discount) as Total_Discount
                 from trialdb.project_trial e
                 inner join project_trial_2 d on e.order_id=d.order_id
                 group by e.category""")
out=mycursor.fetchall()
q_3=pd.DataFrame(out,columns=['Category','Total Discount'])



### Q-4
mycursor.execute("""Select sub_category,AVG(sale_price) as Average
                 From trialdb.project_trial_2
                 group by sub_category""")
out=mycursor.fetchall()
q_4=pd.DataFrame(out,columns=['Sub-Category','Average'])


### Q-5
mycursor.execute("""Select e.region,AVG(d.sale_price) AS `Maximum Average`
                 From trialdb.project_trial e
                 inner join project_trial_2 d on e.order_id=d.order_id
                 group by e.region
                 ORDER BY `Maximum Average` DESC
                 LIMIT 1;
                 """)
out=mycursor.fetchall()
q_5=pd.DataFrame(out,columns=['Region','Average '])

### Q-6
mycursor.execute("""Select e.category,SUM(d.profit) As 'Total Profit'
                 From trialdb.project_trial e
                 inner join  project_trial_2 d on e.order_id=d.order_id
                 group by e.category""")
out=mycursor.fetchall()
q_6=pd.DataFrame(out,columns=['Category','Total Profit'])


#### Q-7
mycursor.execute("""Select e.segment,SUM(d.quantity) AS 'Sum Of Quantity'
                 From trialdb.project_trial e
                 inner join project_trial_2 d on e.order_id=d.order_id
                 group by e.segment
                 ORDER BY `Sum Of Quantity` DESC
                 LIMIT 3;""")
out=mycursor.fetchall()
q_7=pd.DataFrame(out,columns=['Segment','Sum Of Quantity'])


#### Q-8
mycursor.execute("""Select e.region,AVG(d.discount_percent) AS 'Discount percentage'
                 From trialdb.project_trial e
                 inner join project_trial_2 d on e.order_id=d.order_id
                 group by e.region""")
out=mycursor.fetchall()
q_8=pd.DataFrame(out,columns=['Region','Discount percentage'])


#### Q-9
mycursor.execute("""Select e.category,SUM(d.profit) AS 'Total Profit'
                 From trialdb.project_trial e
                 inner join project_trial_2 d on e.order_id=d.order_id
                 group by e.category
                 ORDER BY `Total Profit` DESC
                 LIMIT 1
                 """)
out=mycursor.fetchall()
q_9=pd.DataFrame(out,columns=['Region','Discount percentage'])



#### Q-10
mycursor.execute("""Select YEAR(e.order_date) AS 'Year',Sum(d.sale_price*d.quantity) AS 'Total Revenue'
                 From trialdb.project_trial e
                 inner join project_trial_2 d on e.order_id=d.order_id
                 GROUP BY YEAR(e.order_date)""")
out=mycursor.fetchall()
q_10=pd.DataFrame(out,columns=['Year','Total Revenue'])

#### Q-11
mycursor.execute("""Select e.state,AVG(d.profit) AS Profit
                 From trialdb.project_trial e
                 inner join project_trial_2 d on e.order_id=d.order_id
                 Group by e.state
                 ORDER BY `Profit` DESC""")
out=mycursor.fetchall()
q_11=pd.DataFrame(out,columns=['State','Profit'])


### Q-12

mycursor.execute("""Select sub_category,SUM(quantity) AS 'Total'
                 From trialdb.project_trial_2
                 Group by sub_category""")
out=mycursor.fetchall()
q_12=pd.DataFrame(out,columns=['Sub Category','Total Quantity Orderd'])

### Q-13
mycursor.execute("""SELECT COUNT(*) AS Number_of_order
                FROM trialdb.project_trial_2
                WHERE profit > 100;""")
out=mycursor.fetchall()
q_13=pd.DataFrame(out,columns=['Number of order'])



### Q-14
mycursor.execute("""Select sub_category,SUM(profit) as 'Total Profit'
                 From trialdb.project_trial_2
                 group by sub_category
                 ORDER BY `Total Profit` ASC
                 LIMIT 5""")
out=mycursor.fetchall()
q_14=pd.DataFrame(out,columns=['Sub-Category','Profit'])


### Q-15
mycursor.execute("""Select ship_mode,COUNT(ship_mode)
                 From trialdb.project_trial
                 group by ship_mode
                 """)
out=mycursor.fetchall()
q_15=pd.DataFrame(out,columns=['Ship mode','Count'])

### Q-16
mycursor.execute("""Select state,COUNT(state)
                 From trialdb.project_trial
                 group by state""")
out=mycursor.fetchall()
q_16=pd.DataFrame(out,columns=['State','Count'])


#### Q-17
mycursor.execute("""Select sub_category,AVG(discount)
                 From trialdb.project_trial_2
                 group by sub_category""")
out=mycursor.fetchall()
q_17=pd.DataFrame(out,columns=['Sub Category','Average Discount Price'])


#### Q-18
mycursor.execute("""Select e.segment,AVG(d.sale_price*d.quantity) as Revenue
                 From trialdb.project_trial e
                 inner join project_trial_2 d on e.order_id=d.order_id
                 group by e.segment""")
out=mycursor.fetchall()
q_18=pd.DataFrame(out,columns=['Segment','Average Revenue'])


#### Q-19
mycursor.execute("""Select sub_category,SUM(cost_price)
                 From trialdb.project_trial_2
                 group by sub_category
                 """)
out=mycursor.fetchall()
q_19=pd.DataFrame(out,columns=['Sub Category','Total Amount Spend'])



#### Q-20
mycursor.execute("""Select segment,COUNT(segment)
                 From trialdb.project_trial
                 group by segment""")
out=mycursor.fetchall()
q_20=pd.DataFrame(out,columns=['Segment','Count'])


### Preset Questions
que_1='Top 10 highest revenue generating products'
que_2='The top 5 cities with the highest profit margins'
que_3='Total discount given for each category'
que_4='The average sale price per product category'
que_5='The region with the highest average sale price'
que_6='The total profit per category'
que_7='Top 3 segments with the highest quantity of orders'
que_8='The average discount percentage given per region'
que_9='The product category with the highest total profit'
que_10='Total revenue generated per year'

###Own Questions
que_11='Average Profit per State'
que_12='Total Quantity per Sub category'
que_13='Total Number of oders which has profit more than 100'
que_14='Top 5 Least Profit Sub category'
que_15='Total oders per Ship mode'
que_16='Total number of orders in each state'
que_17='Average discount given per Sub category'
que_18='Average Revenue per segment'
que_19='Total Cost price spend on each Sub category'
que_20='Total Number of orders each segment'



st.title("Retail Order Data Analysis 📊")
st.write("Welcome to our Retail Order Data Analysis page! Here, we provide powerful insights into your retail operations by transforming raw order data into actionable intelligence")
st.header("Preset Queries")
w_input=st.selectbox("Select the Query",[que_1,que_2,que_3,que_4,que_5,que_6,que_7,que_8,que_9,que_10,])
if w_input==que_1:
    st.write(q_1.to_html(index=False),unsafe_allow_html=True)
   # st.bar_chart(q_1.set_index('Product_id')['Revenue'])
elif w_input==que_2:   
    st.write(q_2.to_html(index=False),unsafe_allow_html=True) 
elif w_input==que_3:   
    st.write(q_3.to_html(index=False),unsafe_allow_html=True)
   # st.bar_chart(q_3.set_index('Category')['Total Discount'])
elif w_input==que_4:   
    st.write(q_4.to_html(index=False),unsafe_allow_html=True) 
    st.bar_chart(q_4.set_index('Sub-Category')['Average'])
elif w_input==que_5:   
    st.write(q_5.to_html(index=False),unsafe_allow_html=True)  
elif w_input==que_6:   
    st.write(q_6.to_html(index=False),unsafe_allow_html=True)
   # st.bar_chart(q_6.set_index('Category')['Total Profit'])
elif w_input==que_7:   
    st.write(q_7.to_html(index=False),unsafe_allow_html=True)  
elif w_input==que_8:   
    st.write(q_8.to_html(index=False),unsafe_allow_html=True)
   # st.bar_chart(q_8.set_index('Region')['Discount percentage'])
elif w_input==que_9:   
    st.write(q_9.to_html(index=False),unsafe_allow_html=True)  
elif w_input==que_10:   
    st.write(q_10.to_html(index=False),unsafe_allow_html=True)                              


st.header("Own Queries")
w_input=st.selectbox("Select Own Query",[que_11,que_12,que_13,que_14,que_15,que_16,que_17,que_18,que_19,que_20,])
if w_input==que_11:
    st.write(q_11.to_html(index=False),unsafe_allow_html=True)
    st.bar_chart(q_11.set_index('State')['Profit'])
elif w_input==que_12:   
    st.write(q_12.to_html(index=False),unsafe_allow_html=True)
    st.bar_chart(q_12.set_index('Sub Category')['Total Quantity Orderd'])
elif w_input==que_13:   
    st.write(q_13.to_html(index=False),unsafe_allow_html=True)  
elif w_input==que_14:   
    st.write(q_14.to_html(index=False),unsafe_allow_html=True)  
elif w_input==que_15:   
    st.write(q_15.to_html(index=False),unsafe_allow_html=True)
    st.bar_chart(q_15.set_index('Ship mode')['Count'])
elif w_input==que_16:   
    st.write(q_16.to_html(index=False),unsafe_allow_html=True) 
    st.bar_chart(q_16.set_index('State')['Count'])
elif w_input==que_17:   
    st.write(q_17.to_html(index=False),unsafe_allow_html=True)
    st.bar_chart(q_17.set_index('Sub Category')['Average Discount Price'])  
elif w_input==que_18:   
    st.write(q_18.to_html(index=False),unsafe_allow_html=True)  
elif w_input==que_19:   
    st.write(q_19.to_html(index=False),unsafe_allow_html=True)
    st.bar_chart(q_19.set_index('Sub Category')['Total Amount Spend'])  
elif w_input==que_20:   
    st.write(q_20.to_html(index=False),unsafe_allow_html=True)
    st.bar_chart(q_20.set_index('Segment')['Count'])                              

      





