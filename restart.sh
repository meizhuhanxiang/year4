ps -ef | grep preseller_service | grep gsteps | grep -v grep | awk '{print $2}' | xargs kill -9
nohup python preseller_service.py &
