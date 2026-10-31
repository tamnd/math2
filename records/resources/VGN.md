---
records:
    - id: VGNWFRR7E8
      kind: monograph
      title: Fermat’s Last Theorem
      creators:
        - name: Takeshi Saito
          role: author
      date: "2013-11-01"
      expressions:
        - key: e1
          kind: edition
          date: "2013-11-01"
          ids:
            doi:
                - 10.1090/mmono/243
                - 10.1090/mmono/245
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "2013-11-01"
              ids:
                isbn:
                    - "9780821898482"
                    - "9781470411107"
                    - "9781470416270"
                    - "9781470438401"
            - key: m2
              kind: print
              publisher: American Mathematical Society
              date: "2014-12-12"
              ids:
                isbn:
                    - "9780821898499"
                    - "9781470420444"
                    - "9781470420529"
                    - "9781470438418"
      relations:
        - kind: part_of
          to: BTDY0N3WC9
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/mmono/243
          level: work
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/mmono/245
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
