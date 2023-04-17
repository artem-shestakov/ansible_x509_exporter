import testinfra.utils.ansible_runner
import os


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_service(host):
    service = host.service("x509_certificate_exporter.service")
    assert service.is_enabled
    assert service.is_running

def test_port(host):
    assert host.socket("tcp://9793").is_listening
