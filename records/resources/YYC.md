---
records:
    - id: YYC3BF9439
      kind: problem-set
      title: IMO 2023 Shortlist
      date: "2023"
      expressions:
        - key: e1
          kind: edition
          date: "2023"
      scope:
        value: deferred
        until: "2027-01-29"
        reason: no test decides the record, and the classifier has no model
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: imo
          snapshot: blake3:c564548c1a7c5bfe4e71cf81d61c599a9d4016d698feff8fb0bc9beb0e2f88f9
          native_id: 2023-sl
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to deferred
    - id: YYCNVSWKC4
      kind: monograph
      title: A Course in Minimal Surfaces
      creators:
        - name: Tobias Colding
          role: author
        - name: William Minicozzi
          role: author
      date: "2011-04-01"
      expressions:
        - key: e1
          kind: edition
          date: "2011-04-01"
          ids:
            doi: 10.1090/gsm/121
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "2011-04-01"
              ids:
                isbn:
                    - "9780821853238"
                    - "9780821884232"
                    - "9781470411824"
      relations:
        - kind: part_of
          to: YBEDX3XNVA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/gsm/121
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
