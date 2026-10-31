---
records:
    - id: 1VH1MS8EAB
      kind: monograph
      title: 'Operators, Functions, and Systems: An Easy Reading'
      creators:
        - name: Nikolai Nikolski
          role: author
      date: "2009-09-04"
      expressions:
        - key: e1
          kind: edition
          date: "2009-09-04"
          ids:
            doi:
                - 10.1090/surv/092
                - 10.1090/surv/093
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "2009-09-04"
              ids:
                isbn:
                    - "9780821849330"
                    - "9781470413194"
            - key: m2
              kind: print
              publisher: American Mathematical Society
              date: "2010-10-06"
              ids:
                isbn:
                    - "9780821852651"
                    - "9781470413200"
      relations:
        - kind: part_of
          to: M891DMMNP3
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/surv/092
          level: work
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/surv/093
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
