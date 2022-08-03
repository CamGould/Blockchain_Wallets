<h1 align="center">Creating a Blockchain Wallet on a Local Host</h1>
<h2 align="center">A Hypothetical Solution for Sending Cryptocurrencies to FinTech Professionals</h2>
<h4 align="center"> Created by <em>Cam Gould</em> for the <em>University of Toronto Fintech BootCamp</em> </h4>

<p align="center">
  <img
    src="https://github.com/CamGould/Blockchain_Wallets/blob/main/Supplemental/Streamlit_gif.gif?raw=true"
  >
</p>

### Background Information
For this hypothetical reality, pretend I work at a startup that is building a new and disruptive platform called Fintech Finder. Fintech Finder is an application that its customers can use to find fintech professionals from among a list of candidates, hire them, and pay them. As Fintech Finder’s lead developer, I have been tasked with integrating the *Ethereum blockchain network* into the application in order to enable your customers to instantly pay the fintech professionals whom they hire with cryptocurrency.
<br>
<br>
In this challenge, I will complete the code that enables my customers to send cryptocurrency payments to fintech professionals. To develop the code and test it out, I will assume the perspective of a Fintech Finder customer who is using the application to find a fintech professional and pay them for their work.
<br>
### Project Files
Use the following links to jump right into the anaylsis notebook or view results:
<br>
<br>
This notebook [hosts the functions](https://github.com/CamGould/Blockchain_Wallets/blob/main/Coding%20Notebooks/crypto_wallet.py) I will call into the other notebook
<br>
This notebook contains the code to run the [Transactions using Blockchain within Streamlit](https://github.com/CamGould/Blockchain_Wallets/blob/main/Coding%20Notebooks/fintech_finder.py)

### Project Outline and Instructions
#### Prepare the Data for Training and Testing
1. Create a Jupyter Notebook for each RNN.
2. For the Fear and Greed model, use the FNG values to try and predict the closing price.
3. For the closing price model, use previous closing prices to try and predict the next closing price. 
4. Each model will need to use 70% of the data for training and 30% of the data for testing.
5. Apply a MinMaxScaler to the X and y values to scale the data for the model.
6. Reshape the X_train and X_test values to fit the model's requirement of samples, time steps, and features.

#### Build and Train LSTM RNNs
1. In each Jupyter Notebook, create the same custom LSTM RNN architecture. 
    1. In the first notebook, fit the data using the FNG values. 
    2. In the second notebook, fit the data using only closing prices.

###  Key Findings and Visuals 
#### Visual Price Predictions of Each Model:
***The Model using Closing Price*** - the far better performing model:
<br>
![](https://github.com/CamGould/Deep_Learning_using_LSTM/blob/main/Supplemental/Closing_graph.png?raw=true)
<br>
<br>
***The Model using FNG Indicators*** - a poor performing model:
<br>
![](https://github.com/CamGould/Deep_Learning_using_LSTM/blob/main/Supplemental/FNG_graph.png?raw=true)
<br>
<br>

#### Evaluating the Performance of Each Model

*Which model has a lower loss?*
<br> 
The loss value for each epoch in the training and validation stage displays how well the model is behaving after each stage of its optimization. After looking at how the models each performed, it is no suprise that the **Closing Price Model** had a lower loss than the *FNG Model*. The results for eachof these can be found in their notebooks when the model is running the epochs.
<br>
<br>
*Which model tracks the actual values better over time?*
<br>
When comparing the two graphs of the outputs of each model it is not hard to tell that the **Closing Price Model** tracked the actual values far better. If the two models were closer, and we could not tell right away from the visuals, I would take the average distance the model's price prediction was off of the actual price to determine this answer.
<br>
<br>
*Which window size works best for the models?*
In the end I decided to go with a 10-day closing price window. I found that by having a larger window, the model was predicting prices. using smoother data. This in return helped to minimize some of the outliers, or extremes, that were effecting the model's accuracy of predictions.
