---
records:
    - id: 3MYKYE604Q
      kind: monograph
      title: Applied Functional Analysis
      creators:
        - name: Eberhard Zeidler
          role: author
      date: "1995"
      msc:
        - code: 46-01
          from: zbmath_search
        - code: 47-01
          from: zbmath_search
        - code: 81-01
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1995"
          ids:
            doi:
                - 10.1007/978-1-4612-0815-0
                - 10.1007/978-1-4612-0821-1
            zbl: "0834.46003"
            zbl_id: "780259"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1995"
              ids:
                isbn:
                    - "9781461269106"
                    - "9781461208150"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1995"
              ids:
                isbn:
                    - "9781461269137"
                    - "9781461208211"
              access:
                class: record
      relations:
        - kind: part_of
          to: 2M0N86YNGA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-0815-0
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-0821-1
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "780259"
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
