pipeline 
{
    agent any
    stages 
    {
        stage('Clone') 
        { 
            steps 
            {
                git branch: 'main',url: 'https://github.com/DanilFarafonov/MLops_1-final_task'
            }
        }       
        stage ('создание виртуального окружения') 
        {
            steps 
            {
                sh 'python3 -m venv venv'  
                sh '. venv/bin/activate'
            }
        }
        stage ('скачивание и установка библиотек') 
        {
            steps 
            {
                sh 'pip3 --version'
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage ('загрузка данных из dvc') 
        {
            steps 
            {
                sh 'sudo wget https://dvc.org/deb/dvc.list -O /etc/apt/sources.list.d/dvc.list'
                sh 'wget -qO - https://dvc.org/deb/iterative.asc | gpg --dearmor > packages.iterative.gpg'
                sh 'sudo install -o root -g root -m 644 packages.iterative.gpg /etc/apt/trusted.gpg.d/'
                sh 'rm -f packages.iterative.gpg'
                sh 'sudo apt install dvc'
                sh 'dvc fetch data/y_test.csv'
                sh 'dvc fetch data/y_train.csv'
                sh 'dvc fetch data/x_test.csv'
                sh 'dvc fetch data/x_train.csv'
                sh 'dvc pull'
            }
        }
        stage ('создание модели') 
        {
            steps 
            {
                sh 'python3 model_creation.py'
            }
        }
        stage ('тестирование модели') 
        {
            steps 
            {
                sh 'python3 model_testing.py'
            }
        }
        stage ('Docker build') 
        {
            steps 
            {
                sh 'sudo docker build -t fashion -f Dockerfile .'
            }
        }
        stage ('Docker start') 
        {
            steps 
            {
                sh 'sudo docker run -p 8081:8081 fashion'
            }
        }
    }     
} 
