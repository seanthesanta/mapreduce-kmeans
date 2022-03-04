#!/bin/bash
rm new_cens.pkl old_cens.pkl init_cens.pkl diff.log new_cens
python init_cens.py
cp init_cens.pkl old_cens.pkl

MAX_ITER=150

for ITER in {1..150}
do
    hdfs dfs -rm -r out
    hadoop jar /usr/hdp/2.4.2.0-258/hadoop-mapreduce/hadoop-streaming.jar -D mapred.job.name="Round_$ITER/$MAX_ITER" -D mapred.map.tasks=21 -D mapred.reduce.tasks=7 -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input train_images -output out -file old_cens.pkl
    rm new_cens
    hdfs dfs -cat out/* >> new_cens
    if [[ $(python check.py) == "STOP" ]]
    then
        printf "CONVERGED: BELOW THRESHOLD\n"
        break
    else
        rm old_cens.pkl
        mv new_cens.pkl old_cens.pkl
    fi
done
mv new_cens final_cens
rm new_cens.pkl old_cens.pkl
hdfs dfs -rm -r out
hadoop jar /usr/hdp/2.4.2.0-258/hadoop-mapreduce/hadoop-streaming.jar -D mapred.job.name="Assign" -D mapred.map.tasks=10 -D mapred.reduce.tasks=2 -file assign_mapper.py -mapper assign_mapper.py -file assign_reducer.py -reducer assign_reducer.py -input train_images -output out -file final_cens
hdfs dfs -cat out/* >> tmp
sort -k1 -n tmp >> assign
rm tmp
python accuracy.py
