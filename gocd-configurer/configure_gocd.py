#!/usr/bin/env python
from gomatic import *
import os

def _create_pipeline(group, pipeline_name):
  pipeline_group = configurator.ensure_pipeline_group(group)
  pipeline = pipeline_group.ensure_replacement_of_pipeline(pipeline_name)
  pipeline.ensure_environment_variables({"SHELL": "/bin/bash"})
  return pipeline

def _add_exec_task(job, command, working_dir=None, runif="passed"):
  job.add_task(ExecTask(['/bin/bash', '-l', '-c', command], working_dir=working_dir, runif=runif))

def build_pricing_pipeline_group(configurator):
  pipeline = _create_pipeline("pricing", "pricing-unit-tests")
  pipeline.set_git_url("https://github.com/ThoughtWorks-AELab/pretend_pricing_service")
  job = pipeline.ensure_stage("test").ensure_job("test")
  _add_exec_task(job, 'bundle install --path vendor/bundle --without production')
  _add_exec_task(job, 'bundle exec rake db:migrate')
  _add_exec_task(job, 'bundle exec rake spec:unit')
  job.ensure_artifacts({TestArtifact("spec/reports")})

configurator = GoCdConfigurator(HostRestClient("go-server:8153"))
configurator.remove_all_pipeline_groups()
build_pricing_pipeline_group(configurator)
configurator.save_updated_config()
