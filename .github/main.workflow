workflow "New workflow" {
  on = "push"
  resolves = ["Run Tests"]
}

action "Build Docker Image" {
  uses = "actions/docker/cli@master"
  args = "build -t address_resolver ."
}

action "Run Tests" {
  uses = "actions/docker/cli@master"
  args = "run --rm address_resolver"
  needs = ["Build Docker Image"]
}
