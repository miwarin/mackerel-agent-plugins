%define _binaries_in_noarch_packages_terminate_build   0

%define __buildroot %{_builddir}/%{name}
%define __targetdir /usr/bin

Summary: Monitoring program metric plugins for Mackerel
Name: mackerel-agent-plugins
Version: %{_version}
Release: 1%{?dist}
License: ASL 2.0
Group: Applications/System
URL: https://mackerel.io/

Source0: README.md
Packager:  Hatena
BuildArch: %{buildarch}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This package provides metric plugins for Mackerel.

%prep

%install
%{__rm} -rf %{buildroot}

%{__mkdir} -p %{buildroot}%{__targetdir}

%{__install} -m0755 %{_sourcedir}/build/mackerel-plugin %{buildroot}%{__targetdir}/

for i in accesslog apache2 aws-dynamodb aws-ec2-cpucredit aws-elasticache aws-elasticsearch aws-elb aws-kinesis-streams aws-lambda aws-rds aws-ses conntrack elasticsearch flume gostats graphite haproxy jmx-jolokia jvm linux mailq memcached mongodb multicore munin mysql nginx nvidia-smi openldap php-apc php-fpm php-opcache plack postgres proc-fd solr rabbitmq redis sidekiq snmp squid td-table-count trafficserver twemproxy uwsgi-vassal varnish xentop aws-cloudfront aws-ec2-ebs fluentd docker unicorn uptime inode h2o; do \
    ln -s ./mackerel-plugin %{buildroot}%{__targetdir}/mackerel-plugin-$i; \
done

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{__targetdir}/*

%changelog
* Wed Jan 10 2018 <mackerel-developers@hatena.ne.jp> - 0.42.0
- Move mackerel-plugin-json to other repository (by shibayu36)
- Move mackerel-plugin-gearmand (by shibayu36)
- Move to mackerelio/mackerel-plugin-gcp-compute-engine (by shibayu36)
- [mongodb] fix connections_current metric mongodb-Replica-Set (by vfa-cancc)
- [haproxy]support unix domain socket (by hbadmin)
- [postgres]state may be null even in old versions (by matsuu)
- [uptime] use go-osstat/uptime instead of golib/uptime for getting more accurate uptime (by Songmu)
- [mysql] add a hint for -disable_innodb (by astj)

* Wed Dec 20 2017 <mackerel-developers@hatena.ne.jp> - 0.41.1
- [mysql] set Diff: true for some stats which are actually counter values (by astj)

* Wed Dec 20 2017 <mackerel-developers@hatena.ne.jp> - 0.41.0
- [mysql] Fix some InnoDB stats (by astj)
- [mysql] Fix message for socket option (by utisam)
- MySQL Plugin support Aurora reader node (by dozen)

* Tue Dec 12 2017 <mackerel-developers@hatena.ne.jp> - 0.40.0
- Add h2o to package (by astj)
- Redis Plugin supports custom CONFIG command (by dozen)
- add mackerel-plugin-h2o (by hayajo)
- add defer to closing the response body, and change position it. (by qt-luigi)
- add that close the response body (by qt-luigi)
- [redis] Add Redis replication delay and lag metrics (by kizkoh)

* Tue Nov 28 2017 <mackerel-developers@hatena.ne.jp> - 0.39.0
- Don't add plugins README which has been moved (by astj)
- Improve docker plugin (by astj)
- [jvm] Fix remote jvm monitoring (by astj)
- Changed README.md of mackerel-plugin-linux (by soudai)
- [json] Fix error handling (by astj)
- Fix license notice (by itchyny)
- [docker] Avoid concurrent map writes by multiple goroutines (by astj)
- [aws-ec2-ebs] Do not log "fetched no datapoints" error (by astj)
- [kinesis-streams] Use Sum aggregation for Kinesis streams statistics (by itchyny)

* Thu Nov 09 2017 <mackerel-developers@hatena.ne.jp> - 0.38.0
- Improve mackerel-plugin-postgres (by astj)
- [docker] Add CPU Percentage metrics (by astj)
- [gostats] Use go-mackerel-plugin instead of go-mackerel-plugin-helper (by itchyny)
- [mysql]Fix makeBigint calculation (by matsuu)
- [cloudfront] add -metric-key-prefix option (by fujiwara)

* Thu Oct 26 2017 <mackerel-developers@hatena.ne.jp> - 0.37.1
- [multicore] Refactor multicore plugin (by itchyny)

* Thu Oct 19 2017 <mackerel-developers@hatena.ne.jp> - 0.37.0
- Implement mackerel-plugin-mcrouter (by waniji)
- [uptime] use go-mackerel-plugin instead of using go-mackerel-plugin-helper (by Songmu)

* Thu Oct 12 2017 <mackerel-developers@hatena.ne.jp> - 0.36.0
- Add mackerel-plugin-json (by doublemarket)
- [awd-dynamodb] [incompatible] remove `.` from Metrics.Name (by astj)
- [unicorn] Support metric-key-prefix (by astj)
- [aws-elasticsearch] Improve CloudWatch Statistic type and add some metrics (by holidayworking)

* Wed Oct 04 2017 <mackerel-developers@hatena.ne.jp> - 0.35.0
- [twemproxy] [incompatible] add `-enable-each-server-metrics` option (by Songmu)

* Wed Sep 27 2017 <mackerel-developers@hatena.ne.jp> - 0.34.0
- add mackerel-plugin-flume to package (by y-kuno)
- [mysql]add MyISAM related graphs (by matsuu)
- add mackerel-plugin-sidekiq to package (by syou6162)
- build with Go 1.9 (by astj)
- [OpenLDAP] fix get latestCSN (by masahide)
- [aws-dynamodb] Add ReadThrottleEvents metric and fill 0 when *ThrottleEvents metrics are not present (by astj)

* Wed Sep 20 2017 <mackerel-developers@hatena.ne.jp> - 0.33.0
- add mackerel-plugin-nvidia-smi to package (by syou6162)
- [accesslog] Feature/accesslog/customize parser (by karupanerura)
- Fix redundant error by golint in redis.go (by shibayu36)
- add flume plugin (by y-kuno)
- [mysql]add handler graphs (by matsuu)

* Tue Sep 12 2017 <mackerel-developers@hatena.ne.jp> - 0.32.0
- [memcached] add evicted.reclaimed and evicted.nonzero_evictions (by Songmu)
- [mysql]add missed metrics and fix graph definition (by matsuu)
- [Redis] fix expired keys (by edangelion)
- [accesslog] Fix for scanning long lines (by itchyny)

* Wed Aug 30 2017 <mackerel-developers@hatena.ne.jp> - 0.31.0
- [redis] Change queries metric to diff of "total_commands_processed" (by edangelion)
- [aws-dynamodb] Refactor and parallelize CloudWatch request with errgroup (by astj)
- [plack] Don't raise errors when parsing JSON fields failed (by astj)
- [jmx-jolokia] add value to thread graph (by y-kuno)

* Wed Aug 23 2017 <mackerel-developers@hatena.ne.jp> - 0.30.0
- add mackerel-plugin-openldap to package (by astj)
- Add Burst Balance metric for AWS EC2 EBS plugin (by ariarijp)
- Add openldap plugin  (by masahide)

* Wed Aug 02 2017 <mackerel-developers@hatena.ne.jp> - 0.29.1
- [solr] Fix a graph definition for Apache Solr's cumulative metric (by supercaracal)
- [accesslog] Refine LTSV format detection logic (by Songmu)
- [accesslog] Fix testcase (Percentile logic is Fixed up) (by Songmu)

* Wed Jul 26 2017 <mackerel-developers@hatena.ne.jp> - 0.29.0
- [aws-dynamodb] Add TimeToLiveDeletedItemCount metrics (by astj)
- [aws-dynamodb] Adjust options and graph definitions (by astj)
- [mysql] Fix graph label prefixes (by koooge)

* Wed Jun 28 2017 <mackerel-developers@hatena.ne.jp> - 0.28.1
- postgres: add metric-key-prefix (by edangelion)
- [accesslog] add mackerel-plugin-accesslog (by Songmu)
- add mackerel-plugin-aws-dynamodb to package (by astj)
- Use mackerelio/golib/logging as logger, not mackerelio/mackerel-agent/logging (by astj)
- postgres: collect dbsize only if connectable (by mechairoi)
- Support PostgreSQL 9.6 (by mechairoi)
- Add sidekiq plugin (by littlekbt)

* Wed Jun 14 2017 <mackerel-developers@hatena.ne.jp> - 0.28.0
- Add aws-dynamodb plugin (by astj)
- Implemented mackerel-plugin-redash (by yoheimuta)
- Add mackerel-plugin-solr to package (by astj)
- Add test cases and fix issues for apache solr (by supercaracal)

* Wed Jun 07 2017 <mackerel-developers@hatena.ne.jp> - 0.27.2
- disable diff on php-opcache.cache_size because they are gauge value (by matsuu)
- build with Go 1.8 (by Songmu)
- v2 packages (rpm and deb) (by Songmu)
- [aws-rds] Fix "Latency" metric label (by astj)
- Add AWS Kinesis Firehose Plugin (by holidayworking)
- Fixed mackerel-plugin-nginx/README.md (by kakakakakku)

* Tue May 09 2017 <mackerel-developers@hatena.ne.jp> - 0.27.1-1
- [php-fpm] Implement PluginWithPrefix interfarce (by astj)
- Use SetTempfileByBasename to support MACKEREL_PLUGIN_WORKDIR (by astj)
