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

### 2. **Start the Hadoop Cluster Using Docker Compose**

The repository contains a `docker-compose.yml` file that configures a Hadoop cluster. To start the cluster, run the following command in the **GitHub Codespaces** terminal:

```bash
docker-compose up -d
```

This command will spin up the necessary Hadoop components (ResourceManager, NodeManager, etc.) inside Docker containers.

---

### 3. **Prepare the Python Code for Mapper and Reducer**

1. **Task 1: Total Sales per Product Category**
    - Implement the Python Mapper and Reducer to calculate the **total quantity sold** and **total revenue** for each product category.
    - Refer to the provided `mapper_task1.py` and `reducer_task1.py` files in the repository.

2. **Task 2: Average Revenue per Product Category**
    - Implement the Python Mapper and Reducer to calculate the **average revenue per product** for each category.
    - Refer to the provided `mapper_task2.py` and `reducer_task2.py` files in the repository.

---

### 4. **Move Python Scripts and Dataset to Docker Container**

#### **4.1 Move Python Mapper and Reducer to Container**

Copy the mapper and reducer files for both tasks into the Hadoop ResourceManager container:

```bash
docker cp mappers/mapper_task1.py resourcemanager:/opt/hadoop-3.2.1/share/hadoop/mapreduce/
docker cp reducers/reducer_task1.py resourcemanager:/opt/hadoop-3.2.1/share/hadoop/mapreduce/
docker cp mappers/mapper_task2.py resourcemanager:/opt/hadoop-3.2.1/share/hadoop/mapreduce/
docker cp reducers/reducer_task2.py resourcemanager:/opt/hadoop-3.2.1/share/hadoop/mapreduce/
```

For mrjob, copy the following mrjob Python scripts into the ResourceManager container:

```bash
docker cp mrjob/task1_mrjob.py resourcemanager:/opt/hadoop-3.2.1/share/hadoop/mapreduce/
docker cp mrjob/task2_mrjob.py resourcemanager:/opt/hadoop-3.2.1/share/hadoop/mapreduce/
```

#### **4.2 Move the Input Dataset to Container**

Ensure that the dataset (`product_sales.csv`) is uploaded to the container:

```bash
docker cp input/product_sales.csv resourcemanager:/opt/hadoop-3.2.1/share/hadoop/mapreduce/
```

---

### 5. **Connect to the ResourceManager Container**

To run the Hadoop commands, you'll need to connect to the ResourceManager container:

```bash
docker exec -it resourcemanager /bin/bash
```

Navigate to the directory where your Python scripts and data are located:

```bash
cd /opt/hadoop-3.2.1/share/hadoop/mapreduce/
```

---

### 6. **Set Up HDFS for Input Data**

To run the MapReduce job, the input data file needs to be stored in Hadoop’s distributed file system (HDFS).

#### **6.1 Create Directories in HDFS**

Create a directory in HDFS for the input file:

```bash
hadoop fs -mkdir -p /input/sales_data
```

#### **6.2 Upload the Input File to HDFS**

Upload the sales dataset (`product_sales.csv`) to HDFS:

```bash
hadoop fs -put product_sales.csv /input/sales_data/
```

---

### 7. **Execute the Python MapReduce Job Using Hadoop Streaming**

Now, you are ready to run the MapReduce job using Python and Hadoop Streaming. Below are the commands for each task.

#### **7.1 Task 1: Total Sales per Product Category**

Run the job using Hadoop Streaming:

```bash
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -files mapper_task1.py,reducer_task1.py \
    -mapper mapper_task1.py \
    -reducer reducer_task1.py \
    -input /input/sales_data/product_sales.csv \
    -output /output/task1_total_sales
```

#### **7.2 Task 2: Average Revenue per Product Category**

Run the job using Hadoop Streaming:

```bash
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -files mapper_task2.py,reducer_task2.py \
    -mapper mapper_task2.py \
    -reducer reducer_task2.py \
    -input /input/sales_data/product_sales.csv \
    -output /output/task2_avg_revenue
```

---

### 8. **View the Output of the MapReduce Jobs**

After running the jobs, you can view the output stored in HDFS.

#### **8.1 Task 1 Output: Total Sales per Product Category**

```bash
hadoop fs -cat /output/task1_total_sales/part-00000
```

#### **8.2 Task 2 Output: Average Revenue per Product Category**

```bash
hadoop fs -cat /output/task2_avg_revenue/part-00000
```

---

### 9. **Run Python MapReduce Job Using mrjob**

If you prefer to use the `mrjob` framework, follow the steps below.

#### **9.1 Run Locally (Optional for Testing)**

You can test the mrjob MapReduce job locally by running:

```bash
python task1_mrjob.py /path/to/product_sales.csv
```

#### **9.2 Run mrjob on Hadoop Cluster (YARN)**

To run the mrjob MapReduce jobs on a Hadoop cluster, use the following command:

```bash
python task1_mrjob.py -r hadoop hdfs:///input/sales_data/product_sales.csv -o hdfs:///output/task1_total_sales
```

Similarly, for Task 2:

```bash
python task2_mrjob.py -r hadoop hdfs:///input/sales_data/product_sales.csv -o hdfs:///output/task2_avg_revenue
```

---

### 10. **Copy Output from HDFS to Local OS**

Once you have verified the results, copy the output from HDFS to your local file system.

#### **10.1 Copy Output from HDFS**

Use the following command to copy the output from HDFS to the Hadoop directory:

```bash
hadoop fs -get /output /opt/hadoop-3.2.1/share/hadoop/mapreduce/
```

#### **10.2 Copy Output from the Container to Your Local Machine**

Now, exit the ResourceManager container:

```bash
exit
```

Next, copy the output files from the Docker container to your GitHub Codespaces environment:

```bash
docker cp resourcemanager:/opt/hadoop-3.2.1/share/hadoop/mapreduce/output/ ./output/
```

---

### 11. **Submit Your Code and Output**

#### **11.1 Push Your Code and Output to GitHub**

Commit your changes, including the output from the MapReduce job, and push them to your GitHub repository:

```bash
git add .
git commit -m "Completed Python MapReduce with Hadoop Streaming"
git push origin main
```

#### **11.2 Submit the Assignment on GitHub Classroom**

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
