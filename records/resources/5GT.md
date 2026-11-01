---
records:
    - id: 5GTC6F1QEN
      kind: monograph
      title: 'Analytic Number Theory: Proceedings of a Conference in Honor of Paul T. Bateman'
      creators:
        - name: Bruce C. Berndt
          role: editor
        - name: Harold G. Diamond
          role: editor
        - name: Heini Halberstam
          role: editor
        - name: Adolf Hildebrand
          role: editor
      date: "1990"
      msc:
        - code: 00B25
          from: zbmath_search
        - code: 11-06
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1990"
          ids:
            doi:
                - 10.1007/978-1-4612-3464-7
                - 10.1007/978-1-4612-4086-0
            zbl: "0711.00008"
            zbl_id: "49388"
          manifestations:
            - key: m1
              kind: print
              publisher: Birkhäuser Boston
              date: "1990"
              ids:
                isbn:
                    - "9780817634810"
                    - "9781461234647"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Birkhäuser Boston
              date: "1996"
              ids:
                isbn:
                    - "9781461286455"
                    - "9781461240860"
              access:
                class: record
      relations:
        - kind: part_of
          to: VS2PFDMCR5
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-3464-7
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-4086-0
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "49388"
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
