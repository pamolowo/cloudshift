# automation
# CI/CD enabled
# main github Settings -- developer settings -- personal access token
# go to jenkins -- create new item - pipeline - trigger by webhook - add github url -- pipeline by script scm -- git hub-- credential -- add PAT -- SAVE
#  go to github  repo settings -- add webhooks-- payload url --http://jenkinsurl:8080//github-webhook/ -- application json -- on push event