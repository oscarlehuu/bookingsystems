"""Generated client library for composer version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.generated_clients.apis.composer.v1 import composer_v1_messages as messages


class ComposerV1(base_api.BaseApiClient):
  """Generated client library for service composer version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://composer.googleapis.com/'
  MTLS_BASE_URL = 'https://composer.mtls.googleapis.com/'

  _PACKAGE = 'composer'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'ComposerV1'
  _URL_VERSION = 'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new composer handle."""
    url = url or self.BASE_URL
    super(ComposerV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_environments_userWorkloadsConfigMaps = self.ProjectsLocationsEnvironmentsUserWorkloadsConfigMapsService(self)
    self.projects_locations_environments_userWorkloadsSecrets = self.ProjectsLocationsEnvironmentsUserWorkloadsSecretsService(self)
    self.projects_locations_environments_workloads = self.ProjectsLocationsEnvironmentsWorkloadsService(self)
    self.projects_locations_environments = self.ProjectsLocationsEnvironmentsService(self)
    self.projects_locations_imageVersions = self.ProjectsLocationsImageVersionsService(self)
    self.projects_locations_operations = self.ProjectsLocationsOperationsService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsEnvironmentsUserWorkloadsConfigMapsService(base_api.BaseApiService):
    """Service class for the projects_locations_environments_userWorkloadsConfigMaps resource."""

    _NAME = 'projects_locations_environments_userWorkloadsConfigMaps'

    def __init__(self, client):
      super(ComposerV1.ProjectsLocationsEnvironmentsUserWorkloadsConfigMapsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a user workloads ConfigMap. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer.

      Args:
        request: (ComposerProjectsLocationsEnvironmentsUserWorkloadsConfigMapsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (UserWorkloadsConfigMap) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/environments/{environmentsId}/userWorkloadsConfigMaps',
        http_method='POST',
        method_id='composer.projects.locations.environments.userWorkloadsConfigMaps.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1/{+parent}/userWorkloadsConfigMaps',
        request_field='userWorkloadsConfigMap',
        request_type_name='ComposerProjectsLocationsEnvironmentsUserWorkloadsConfigMapsCreateRequest',
        response_type_name='UserWorkloadsConfigMap',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a user workloads ConfigMap. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer.

      Args:
        request: (ComposerProjectsLocationsEnvironmentsUserWorkloadsConfigMapsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/environments/{environmentsId}/userWorkloadsConfigMaps/{userWorkloadsConfigMapsId}',
        http_method='DELETE',
        method_id='composer.projects.locations.environments.userWorkloadsConfigMaps.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='ComposerProjectsLocationsEnvironmentsUserWorkloadsConfigMapsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets an existing user workloads ConfigMap. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer.

      Args:
        request: (ComposerProjectsLocationsEnvironmentsUserWorkloadsConfigMapsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (UserWorkloadsConfigMap) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/environments/{environmentsId}/userWorkloadsConfigMaps/{userWorkloadsConfigMapsId}',
        http_method='GET',
        method_id='composer.projects.locations.environments.userWorkloadsConfigMaps.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='ComposerProjectsLocationsEnvironmentsUserWorkloadsConfigMapsGetRequest',
        response_type_name='UserWorkloadsConfigMap',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists user workloads ConfigMaps. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer.

      Args:
        request: (ComposerProjectsLocationsEnvironmentsUserWorkloadsConfigMapsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListUserWorkloadsConfigMapsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/environments/{environmentsId}/userWorkloadsConfigMaps',
        http_method='GET',
        method_id='composer.projects.locations.environments.userWorkloadsConfigMaps.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1/{+parent}/userWorkloadsConfigMaps',
        request_field='',
        request_type_name='ComposerProjectsLocationsEnvironmentsUserWorkloadsConfigMapsListRequest',
        response_type_name='ListUserWorkloadsConfigMapsResponse',
        supports_download=False,
    )

    def Update(self, request, global_params=None):
      r"""Updates a user workloads ConfigMap. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer.

      Args:
        request: (UserWorkloadsConfigMap) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (UserWorkloadsConfigMap) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

    Update.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/environments/{environmentsId}/userWorkloadsConfigMaps/{userWorkloadsConfigMapsId}',
        http_method='PUT',
        method_id='composer.projects.locations.environments.userWorkloadsConfigMaps.update',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='<request>',
        request_type_name='UserWorkloadsConfigMap',
        response_type_name='UserWorkloadsConfigMap',
        supports_download=False,
    )

  class ProjectsLocationsEnvironmentsUserWorkloadsSecretsService(base_api.BaseApiService):
    """Service class for the projects_locations_environments_userWorkloadsSecrets resource."""

    _NAME = 'projects_locations_environments_userWorkloadsSecrets'

    def __init__(self, client):
      super(ComposerV1.ProjectsLocationsEnvironmentsUserWorkloadsSecretsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a user workloads Secret. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer.

      Args:
        request: (ComposerProjectsLocationsEnvironmentsUserWorkloadsSecretsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (UserWorkloadsSecret) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/environments/{environmentsId}/userWorkloadsSecrets',
        http_method='POST',
        method_id='composer.projects.locations.environments.userWorkloadsSecrets.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1/{+parent}/userWorkloadsSecrets',
        request_field='userWorkloadsSecret',
        request_type_name='ComposerProjectsLocationsEnvironmentsUserWorkloadsSecretsCreateRequest',
        response_type_name='UserWorkloadsSecret',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a user workloads Secret. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer.

      Args:
        request: (ComposerProjectsLocationsEnvironmentsUserWorkloadsSecretsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/environments/{environmentsId}/userWorkloadsSecrets/{userWorkloadsSecretsId}',
        http_method='DELETE',
        method_id='composer.projects.locations.environments.userWorkloadsSecrets.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='ComposerProjectsLocationsEnvironmentsUserWorkloadsSecretsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets an existing user workloads Secret. Values of the "data" field in the response are cleared. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer.

      Args:
        request: (ComposerProjectsLocationsEnvironmentsUserWorkloadsSecretsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (UserWorkloadsSecret) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/environments/{environmentsId}/userWorkloadsSecrets/{userWorkloadsSecretsId}',
        http_method='GET',
        method_id='composer.projects.locations.environments.userWorkloadsSecrets.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='ComposerProjectsLocationsEnvironmentsUserWorkloadsSecretsGetRequest',
        response_type_name='UserWorkloadsSecret',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists user workloads Secrets. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer.

      Args:
        request: (ComposerProjectsLocationsEnvironmentsUserWorkloadsSecretsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListUserWorkloadsSecretsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/environments/{environmentsId}/userWorkloadsSecrets',
        http_method='GET',
        method_id='composer.projects.locations.environments.userWorkloadsSecrets.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1/{+parent}/userWorkloadsSecrets',
        request_field='',
        request_type_name='ComposerProjectsLocationsEnvironmentsUserWorkloadsSecretsListRequest',
        response_type_name='ListUserWorkloadsSecretsResponse',
        supports_download=False,
    )

    def Update(self, request, global_params=None):
      r"""Updates a user workloads Secret. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer.

      Args:
        request: (UserWorkloadsSecret) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (UserWorkloadsSecret) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

    Update.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/environments/{environmentsId}/userWorkloadsSecrets/{userWorkloadsSecretsId}',
        http_method='PUT',
        method_id='composer.projects.locations.environments.userWorkloadsSecrets.update',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='<request>',
        request_type_name='UserWorkloadsSecret',
        response_type_name='UserWorkloadsSecret',
        supports_download=False,
    )

  class ProjectsLocationsEnvironmentsWorkloadsService(base_api.BaseApiService):
    """Service class for the projects_locations_environments_workloads resource."""

    _NAME = 'projects_locations_environments_workloads'

    def __init__(self, client):
      super(ComposerV1.ProjectsLocationsEnvironmentsWorkloadsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""Lists workloads in a Cloud Composer environment. Workload is a unit that runs a single Composer component. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer.

      Args:
        request: (ComposerProjectsLocationsEnvironmentsWorkloadsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListWorkloadsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/environments/{environmentsId}/workloads',
        http_method='GET',
        method_id='composer.projects.locations.environments.workloads.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+parent}/workloads',
        request_field='',
        request_type_name='ComposerProjectsLocationsEnvironmentsWorkloadsListRequest',
        response_type_name='ListWorkloadsResponse',
        supports_download=False,
    )

  class ProjectsLocationsEnvironmentsService(base_api.BaseApiService):
    """Service class for the projects_locations_environments resource."""

    _NAME = 'projects_locations_environments'

    def __init__(self, client):
      super(ComposerV1.ProjectsLocationsEnvironmentsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Create a new environment.

      Args:
        request: (ComposerProjectsLocationsEnvironmentsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/environments',
        http_method='POST',
        method_id='composer.projects.locations.environments.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1/{+parent}/environments',
        request_field='environment',
        request_type_name='ComposerProjectsLocationsEnvironmentsCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def DatabaseFailover(self, request, global_params=None):
      r"""Triggers database failover (only for highly resilient environments).

      Args:
        request: (ComposerProjectsLocationsEnvironmentsDatabaseFailoverRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('DatabaseFailover')
      return self._RunMethod(
          config, request, global_params=global_params)

    DatabaseFailover.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/environments/{environmentsId}:databaseFailover',
        http_method='POST',
        method_id='composer.projects.locations.environments.databaseFailover',
        ordered_params=['environment'],
        path_params=['environment'],
        query_params=[],
        relative_path='v1/{+environment}:databaseFailover',
        request_field='databaseFailoverRequest',
        request_type_name='ComposerProjectsLocationsEnvironmentsDatabaseFailoverRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Delete an environment.

      Args:
        request: (ComposerProjectsLocationsEnvironmentsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/environments/{environmentsId}',
        http_method='DELETE',
        method_id='composer.projects.locations.environments.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='ComposerProjectsLocationsEnvironmentsDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def ExecuteAirflowCommand(self, request, global_params=None):
      r"""Executes Airflow CLI command.

      Args:
        request: (ComposerProjectsLocationsEnvironmentsExecuteAirflowCommandRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ExecuteAirflowCommandResponse) The response message.
      """
      config = self.GetMethodConfig('ExecuteAirflowCommand')
      return self._RunMethod(
          config, request, global_params=global_params)

    ExecuteAirflowCommand.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/environments/{environmentsId}:executeAirflowCommand',
        http_method='POST',
        method_id='composer.projects.locations.environments.executeAirflowCommand',
        ordered_params=['environment'],
        path_params=['environment'],
        query_params=[],
        relative_path='v1/{+environment}:executeAirflowCommand',
        request_field='executeAirflowCommandRequest',
        request_type_name='ComposerProjectsLocationsEnvironmentsExecuteAirflowCommandRequest',
        response_type_name='ExecuteAirflowCommandResponse',
        supports_download=False,
    )

    def FetchDatabaseProperties(self, request, global_params=None):
      r"""Fetches database properties.

      Args:
        request: (ComposerProjectsLocationsEnvironmentsFetchDatabasePropertiesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (FetchDatabasePropertiesResponse) The response message.
      """
      config = self.GetMethodConfig('FetchDatabaseProperties')
      return self._RunMethod(
          config, request, global_params=global_params)

    FetchDatabaseProperties.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/environments/{environmentsId}:fetchDatabaseProperties',
        http_method='GET',
        method_id='composer.projects.locations.environments.fetchDatabaseProperties',
        ordered_params=['environment'],
        path_params=['environment'],
        query_params=[],
        relative_path='v1/{+environment}:fetchDatabaseProperties',
        request_field='',
        request_type_name='ComposerProjectsLocationsEnvironmentsFetchDatabasePropertiesRequest',
        response_type_name='FetchDatabasePropertiesResponse',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Get an existing environment.

      Args:
        request: (ComposerProjectsLocationsEnvironmentsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Environment) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/environments/{environmentsId}',
        http_method='GET',
        method_id='composer.projects.locations.environments.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='ComposerProjectsLocationsEnvironmentsGetRequest',
        response_type_name='Environment',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""List environments.

      Args:
        request: (ComposerProjectsLocationsEnvironmentsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListEnvironmentsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/environments',
        http_method='GET',
        method_id='composer.projects.locations.environments.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1/{+parent}/environments',
        request_field='',
        request_type_name='ComposerProjectsLocationsEnvironmentsListRequest',
        response_type_name='ListEnvironmentsResponse',
        supports_download=False,
    )

    def LoadSnapshot(self, request, global_params=None):
      r"""Loads a snapshot of a Cloud Composer environment. As a result of this operation, a snapshot of environment's specified in LoadSnapshotRequest is loaded into the environment.

      Args:
        request: (ComposerProjectsLocationsEnvironmentsLoadSnapshotRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('LoadSnapshot')
      return self._RunMethod(
          config, request, global_params=global_params)

    LoadSnapshot.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/environments/{environmentsId}:loadSnapshot',
        http_method='POST',
        method_id='composer.projects.locations.environments.loadSnapshot',
        ordered_params=['environment'],
        path_params=['environment'],
        query_params=[],
        relative_path='v1/{+environment}:loadSnapshot',
        request_field='loadSnapshotRequest',
        request_type_name='ComposerProjectsLocationsEnvironmentsLoadSnapshotRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Update an environment.

      Args:
        request: (ComposerProjectsLocationsEnvironmentsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/environments/{environmentsId}',
        http_method='PATCH',
        method_id='composer.projects.locations.environments.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1/{+name}',
        request_field='environment',
        request_type_name='ComposerProjectsLocationsEnvironmentsPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def PollAirflowCommand(self, request, global_params=None):
      r"""Polls Airflow CLI command execution and fetches logs.

      Args:
        request: (ComposerProjectsLocationsEnvironmentsPollAirflowCommandRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (PollAirflowCommandResponse) The response message.
      """
      config = self.GetMethodConfig('PollAirflowCommand')
      return self._RunMethod(
          config, request, global_params=global_params)

    PollAirflowCommand.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/environments/{environmentsId}:pollAirflowCommand',
        http_method='POST',
        method_id='composer.projects.locations.environments.pollAirflowCommand',
        ordered_params=['environment'],
        path_params=['environment'],
        query_params=[],
        relative_path='v1/{+environment}:pollAirflowCommand',
        request_field='pollAirflowCommandRequest',
        request_type_name='ComposerProjectsLocationsEnvironmentsPollAirflowCommandRequest',
        response_type_name='PollAirflowCommandResponse',
        supports_download=False,
    )

    def SaveSnapshot(self, request, global_params=None):
      r"""Creates a snapshots of a Cloud Composer environment. As a result of this operation, snapshot of environment's state is stored in a location specified in the SaveSnapshotRequest.

      Args:
        request: (ComposerProjectsLocationsEnvironmentsSaveSnapshotRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('SaveSnapshot')
      return self._RunMethod(
          config, request, global_params=global_params)

    SaveSnapshot.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/environments/{environmentsId}:saveSnapshot',
        http_method='POST',
        method_id='composer.projects.locations.environments.saveSnapshot',
        ordered_params=['environment'],
        path_params=['environment'],
        query_params=[],
        relative_path='v1/{+environment}:saveSnapshot',
        request_field='saveSnapshotRequest',
        request_type_name='ComposerProjectsLocationsEnvironmentsSaveSnapshotRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def StopAirflowCommand(self, request, global_params=None):
      r"""Stops Airflow CLI command execution.

      Args:
        request: (ComposerProjectsLocationsEnvironmentsStopAirflowCommandRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (StopAirflowCommandResponse) The response message.
      """
      config = self.GetMethodConfig('StopAirflowCommand')
      return self._RunMethod(
          config, request, global_params=global_params)

    StopAirflowCommand.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/environments/{environmentsId}:stopAirflowCommand',
        http_method='POST',
        method_id='composer.projects.locations.environments.stopAirflowCommand',
        ordered_params=['environment'],
        path_params=['environment'],
        query_params=[],
        relative_path='v1/{+environment}:stopAirflowCommand',
        request_field='stopAirflowCommandRequest',
        request_type_name='ComposerProjectsLocationsEnvironmentsStopAirflowCommandRequest',
        response_type_name='StopAirflowCommandResponse',
        supports_download=False,
    )

  class ProjectsLocationsImageVersionsService(base_api.BaseApiService):
    """Service class for the projects_locations_imageVersions resource."""

    _NAME = 'projects_locations_imageVersions'

    def __init__(self, client):
      super(ComposerV1.ProjectsLocationsImageVersionsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""List ImageVersions for provided location.

      Args:
        request: (ComposerProjectsLocationsImageVersionsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListImageVersionsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/imageVersions',
        http_method='GET',
        method_id='composer.projects.locations.imageVersions.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['includePastReleases', 'pageSize', 'pageToken'],
        relative_path='v1/{+parent}/imageVersions',
        request_field='',
        request_type_name='ComposerProjectsLocationsImageVersionsListRequest',
        response_type_name='ListImageVersionsResponse',
        supports_download=False,
    )

  class ProjectsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_operations resource."""

    _NAME = 'projects_locations_operations'

    def __init__(self, client):
      super(ComposerV1.ProjectsLocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Delete(self, request, global_params=None):
      r"""Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (ComposerProjectsLocationsOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='DELETE',
        method_id='composer.projects.locations.operations.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='ComposerProjectsLocationsOperationsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (ComposerProjectsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='GET',
        method_id='composer.projects.locations.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='ComposerProjectsLocationsOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.

      Args:
        request: (ComposerProjectsLocationsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/operations',
        http_method='GET',
        method_id='composer.projects.locations.operations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+name}/operations',
        request_field='',
        request_type_name='ComposerProjectsLocationsOperationsListRequest',
        response_type_name='ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(ComposerV1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(ComposerV1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
