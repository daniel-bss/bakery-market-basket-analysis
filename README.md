<img style="width: 100%" src="https://raw.githubusercontent.com/daniel-bss/bakery-market-basket-analysis/main/img/bakeryshop.jpg">
<h3 align="center" style="margin-top: 12px; font-size: 1.5em">Bakery Shop Market Basket Analysis<h3>

<h2>📄Table of Contents</h2>

- [Problem Statement](#problem-statement)
- [Solution](#solution)
- [Getting Started](#getting-started)
  - [Clone Repository](#cloning)
  - [Create and Activate Python Virtual Environment](#creating-env)
  - [Installing Required Packages](#installation)
  - [Running The Application](#running)

<h2 id="problem-statement">🔎Problem Statement</h2>
It is crucial for companies as well as small business to plan their products which are going to put on sale, in intention of maximizing revenue. But quite often happens a situation where products are unbalancedly sold. Some products are sold quickly and some are not likely to be touched.

<h2 id="solution">💡Solution</h2>
Using the given dataset, we would like to help this bakery shop to optimize their sales, by performing Market Basket Analysis to extract information about which item relates to which. For instance, the bakery owner can recommend a customer who buys bread to also buy coffee with special price, because those two items are oftenly bought together.

<h2 id="getting-started">🏃‍♂️Getting Started</h2>
<h3 id="cloning">Clone Repository</h3>
First, easily clone this project into your local machine using this command (make sure you have Git installed).

```
git clone https://github.com/daniel-bss/bakery-market-basket-analysis.git
```
<h3 id="creating-env">Create and Activate Python Virtual Environment</h3>

To keep up with the same environment, make sure you have <b>Python 3.8.x</b> installed. Then install `virtualenv` package.

```
pip install virtualenv
```

<br>
Proceed on creating Virtual Environment.

```
virtualenv venv --python="<THE_PATH_TO_YOUR_PYTHON39_EXECUTABLE_FILE>"
```

>Example on Windows:
```
virtualenv venv --python="C:\Users\JohnDoe\AppData\Local\Programs\Python\Python39\python.exe"
```
<br>
Staying still on the root of your project, go activate your Virtual Environment.

```
venv\Scripts\activate
```

<h3 id="installation">Installing Required Packages</h3>

Following the `requirements.txt`, please install the following packages below using this command: `pip install <package>==1.2.3`

```
numpy==1.23.3
pandas==1.5.0
mlxtend==0.19.0
streamlit==1.5.0
protobuf==3.19.0
click<=8.0.4
```

<h3 id="running">Running The Application</h3>
You have successfully created Virtual Environment with the desired Python version and the required packages. You are now ready to run the Streamlit application using this command.

```
streamlit run main.py
```

<dl>
  <dd>
    <dl>
      <dd>
        <dl>
          <dd>
            <dl>
              <dd>
                <dl>
                  <dd>
                    <dl>
                      <dd>
                        <dl>
                          <dd>
                            <img style="width: 100%;" src="https://raw.githubusercontent.com/daniel-bss/bakery-market-basket-analysis/main/img/webapp.png">
                          </dd>
                        </dl>
                      </dd>
                    </dl>
                  </dd>
                </dl>
              </dd>
            </dl>
          </dd>
        </dl>
      </dd>
    </dl>
  </dd>
</dl>

<p style="margin-top: 100px;" align="center"><i>(Quick look of the Web App. Created with Streamlit, hosted by Heroku)</i></p>
