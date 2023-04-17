# Ansible PostgreSQL exporter
Installs the X.509 Certificate Exporter for Prometheus.

## Role Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `x509_exporter_version` | Version of exporter.  | `3.6.0` |
| `x509_exporter_url`| URL to download tar.gz archive with binary | `https://github.com/enix/x509-certificate-exporter/releases/download/v{{ x509_exporter_version }}/x509-certificate-exporter-linux-amd64.tar.gz` |
| `x509_exporter_dist_dir` | Directory for exporter binary | `/usr/local/bin` |
| `x509_exporter_config_file` | File with exporter `$FLAGS` | `/etc/default/x509_exporter` |
| `x509_exporter_user` | User to run exporter | `prometheus` |
| `x509_exporter_address` | Address on which to bind and expose metrics | `0.0.0.0` |
| `x509_exporter_port` | Pddress on which to bind and expose metrics | `9793` |
| `x509_exporter_flags` | Array of exporter [flags](https://github.com/enix/x509-certificate-exporter#advanced-usage) | `[]` |
>Don't add flag`-b, --listen-address` to `x509_exporter_flags`. It is used in `x509_exporter_config_file` and uses values of `x509_exporter_address` and `x509_exporter_port` variables.

## Example Playbook
```yaml
- hosts: all
  roles:
    - artem_shestakov.x509_exporter
```

## License
GPLv3

## Author Information
artem.s.shestakov@gmail.com
