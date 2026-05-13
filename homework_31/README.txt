запуск docker:
docker pull jenkins/jenkins:2.492.3
docker run -d -p 8080:8080 -p 50000:50000 -v "E:\hillel\homework\homework_02\homework_git\homework_31\jenkins_data:/var/jenkins_home" --name jenkins-server jenkins/jenkins:2.492.3

password: 93b7d11368a440e4ab1b8d6ad2bdb598
docker logs jenkins-server
