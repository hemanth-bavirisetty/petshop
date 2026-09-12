how to run:

to start containers

docker compose up --build



# 1. Log in to your local Concourse
fly -t local login -c http://localhost:8080 -u admin -p admin

# 2. Update ci/pipeline.yml with YOUR repo URL (the one you just pushed):
#    uri: https://github.com/<your-username>/petshop.git

# 3. Push the pipeline config and start it
fly -t local set-pipeline -p petshop -c ci/pipeline.yml
fly -t local unpause-pipeline -p petshop

# 4. Kick off the first run manually (after this, pushes trigger it automatically)
fly -t local trigger-job -j petshop/test --watch

