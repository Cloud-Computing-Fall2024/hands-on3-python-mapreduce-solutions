Here’s the project setup and detailed instructions for **Hands-on 3: Python MapReduce Using Hadoop Streaming or mrjob**:
# Hands-on 3: Python MapReduce with Hadoop Streaming or mrjob

This hands-on activity will focus on using **Python** to implement MapReduce jobs. You will use two frameworks for this task: **Hadoop Streaming** or **mrjob**. You will analyze a simple dataset, similar to previous activities, but implement the Mapper and Reducer in Python.

## **Objectives**

By completing this hands-on activity, students will:

1. **Gain Experience with Python for MapReduce:** Learn how to implement mappers and reducers in Python using Hadoop Streaming or the `mrjob` framework.
2. **Understand Basic Python MapReduce Concepts:** Develop an understanding of how to write Python code for MapReduce and run it on a Hadoop cluster.
3. **Deploy and Run Python MapReduce on Hadoop:** Learn how to deploy and execute MapReduce jobs written in Python using Hadoop Streaming or `mrjob`.
4. **Submit and Manage Code Using GitHub:** Develop skills in managing code and submitting assignments via GitHub.

---

## **Setup and Execution**

### 1. **Fork the GitHub Repository**

- First, accept the GitHub Classroom invitation and fork the assignment repository to your own GitHub account.
- Once you’ve forked the repo, open the repository in **GitHub Codespaces** to begin working on the assignment.

---

### 2. **Install the Hadoop Cluster on any Virtual Machine**

#### For Windows Users:
- Download virtual box from this [link](https://www.virtualbox.org/)
- Download the iso file for Ubuntu from this [link](https://ubuntu.com/download/desktop)
- After installing and setting up the ubuntu VM follow the instruction that are given in the lecture slides to setup hadoop on a VM

#### For Mac User:
- For mac user installing hadoop doesn't require any additional VM on top of Macos
- You can follow the instruction given in this article to install hadoop natively on mac book
- [Click here](https://medium.com/@vikramus4/install-and-configure-hadoop-3-3-6-in-mac-os-dd4be4da8846) to install hadoop on macos

---

### 3. **Prepare the Python Code for Mapper and Reducer**

1. **Task 1: Total Sales per Product Category**
    - Implement the Python Mapper and Reducer to calculate the **total quantity sold** and **total revenue** for each product category.
    - Refer to the provided `mapper_task1.py` and `reducer_task1.py` files in the repository.

2. **Task 2: Average Revenue per Product Category**
    - Implement the Python Mapper and Reducer to calculate the **average revenue per product** for each category.
    - Refer to the provided `mapper_task2.py` and `reducer_task2.py` files in the repository.

---

### 4. Clone the Github repo into your VM (for windows)

- After accepting the assignment in the github classroom you will be given a repository into you github profile
- Clone the repository into your appropriate VM
- Finish the code for both tasks

### 5. **Set Up HDFS for Input Data**

To run the MapReduce job, the input data file needs to be stored in Hadoop’s distributed file system (HDFS).

#### **5.1 Create Directories in HDFS**

Create a directory in HDFS for the input file:

```bash
hadoop fs -mkdir -p /input/sales_data
```

#### **5.2 Upload the Input File to HDFS**

Upload the sales dataset (`product_sales.csv`) to HDFS:

```bash
hadoop fs -put product_sales.csv /input/sales_data/
```

---

### 6. **Execute the Python MapReduce Job Using Hadoop Streaming (prefer to run in VM to get required output)**

Now, you are ready to run the MapReduce job using Python and Hadoop Streaming. Below are the commands for each task.

#### **6.1 Task 1: Total Sales per Product Category**

Run the job using Hadoop Streaming:

```bash
mapred streaming 
    -files mapper_task1.py,reducer_task1.py 
    -mapper mapper_task1.py 
    -reducer reducer_task1.py 
    -input /input/sales_data/product_sales.csv 
    -output /output/task1_total_sales
```
   or

```bash

   hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar  -files /home/hadoop/Downloads/hadoop-streaming-and-mrjob-main/mappers/mapper_task1.py,/home/hadoop/Downloads/hadoop-streaming-and-mrjob-main/reducers/reducer_task1.py  -mapper mapper_task1.py  -reducer reducer_task1.py  -input /input/product_sales.csv -output /output/task1_total_sales   

```
   or
```bash
   
   hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar  -files /home/hadoop/Downloads/hadoop-streaming-and-mrjob-main/mappers/mapper_task1.py,/home/hadoop/Downloads/hadoop-streaming-and-mrjob-main/reducers/reducer_task1.py  -mapper "python3 mapper_task1.py"  -reducer "python3 reducer_task1.py"  -input /input/product_sales.csv -output /output/task1_total_sales
```


#### **6.2 Task 2: Average Revenue per Product Category**

Run the job using Hadoop Streaming:

```bash
mapred streaming 
    -files mapper_task1.py,reducer_task1.py 
    -mapper mapper_task1.py 
    -reducer reducer_task1.py 
    -input /input/sales_data/product_sales.csv 
    -output /output/task1_total_sales
```

---

### 7. **View the Output of the MapReduce Jobs**

After running the jobs, you can view the output stored in HDFS.

#### **7.1 Task 1 Output: Total Sales per Product Category**

```bash
hadoop fs -cat /output/task1_total_sales/part-00000
```

#### **7.2 Task 2 Output: Average Revenue per Product Category**

```bash
hadoop fs -cat /output/task2_avg_revenue/part-00000
```

---

### 8. **Run Python MapReduce Job Using mrjob**

If you prefer to use the `mrjob` framework, follow the steps below.

#### **8.1 Run Locally (Optional for Testing)**

You can test the mrjob MapReduce job locally by running:

```bash
python3 task1_mrjob.py /path/to/product_sales.csv
```

#### **8.2 Run mrjob on Hadoop Cluster (YARN)**

To run the mrjob MapReduce jobs on a Hadoop cluster, use the following command:

```bash
python3 task1_mrjob.py -r hadoop hdfs:///input/sales_data/product_sales.csv -o hdfs:///output/task1_total_sales
```

Similarly, for Task 2:

```bash
python3 task2_mrjob.py -r hadoop hdfs:///input/sales_data/product_sales.csv -o hdfs:///output/task2_avg_revenue
```

---

### 9. **Copy Output from HDFS to Local OS**

Once you have verified the results, copy the output from HDFS to your local file system.

#### **9.1 Copy Output from HDFS**

Use the following command to copy the output from HDFS to the Hadoop directory:

```bash
hadoop fs -get /output /opt/hadoop-3.2.1/share/hadoop/mapreduce/
```

#### **9.2 Copy Output from the Container to Your Local Machine**

Now, exit the ResourceManager container:

```bash
exit
```

Next, copy the output files from the Docker container to your GitHub Codespaces environment:

```bash
docker cp resourcemanager:/opt/hadoop-3.2.1/share/hadoop/mapreduce/output/ ./output/
```

---

### 10. **Submit Your Code and Output**

#### **10.1 Push Your Code and Output to GitHub**

Commit your changes, including the output from the MapReduce job, and push them to your GitHub repository:

```bash
git add .
git commit -m "Completed Python MapReduce with Hadoop Streaming"
git push origin main
```

#### **10.2 Submit the Assignment on GitHub Classroom**

Once you've pushed your code, go to GitHub Classroom and ensure your repository is submitted for the assignment. Make sure that the following are included:

1. Python scripts for Mapper and Reducer.
2. The input file (`product_sales.csv`).
3. The output files from your MapReduce job.
4. A one-page report documenting the steps you followed, any challenges faced, and your observations.

---

### **Grading Criteria**

1. **Correct Implementation of Python MapReduce Jobs:** The MapReduce jobs must correctly process the dataset and produce the expected results.
2. **Proper Use of Hadoop Streaming or mrjob:** Your solution must show correct implementation using Hadoop Streaming or mrjob.
3. **Submission of Code and Output:** The correct output should be produced and submitted via GitHub, along with the Python code and a brief report.
4. **Report:** A clear and concise one-page report summarizing your setup, challenges, and observations.

---

This concludes the instructions for the hands-on activity. If you encounter any issues, feel free to reach out during office hours or post your queries in the course discussion forum.

Good luck, and happy coding!
