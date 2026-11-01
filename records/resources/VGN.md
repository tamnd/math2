---
records:
    - id: VGNWFRR7E8
      kind: monograph
      title: Fermat’s Last Theorem
      creators:
        - name: Takeshi Saito
          role: author
      date: "2013-11-01"
      msc:
        - code: 11-02
          from: zbmath_search
        - code: 11G05
          from: zbmath_search
        - code: 11F11
          from: zbmath_search
        - code: 11F80
          from: zbmath_search
        - code: 11G18
          from: zbmath_search
        - code: 11D41
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2013-11-01"
          ids:
            doi:
                - 10.1090/mmono/243
                - 10.1090/mmono/245
            zbl: "1311.11004"
            zbl_id: "6198401"
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
              access:
                class: record
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
              access:
                class: record
      relations:
        - kind: part_of
          to: BTDY0N3WC9
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/mmono/243
          level: work
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/mmono/245
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "6198401"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
