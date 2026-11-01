---
records:
    - id: PHNY20PP0J
      kind: monograph
      title: Applied Abstract Algebra
      creators:
        - name: Rudolf Lidl
          role: author
        - name: Günter Pilz
          role: author
      date: "1984"
      msc:
        - code: 00-01
          from: zbmath_search
        - code: 00A69
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1984"
          ids:
            doi:
                - 10.1007/978-1-4615-6465-2
                - 10.1007/978-1-4757-2941-2
            zbl: "0572.00001"
            zbl_id: "3912289"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer US
              date: "1984"
              ids:
                isbn:
                    - "9780387961668"
                    - "9781461564652"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1998"
              ids:
                isbn:
                    - "9781441931177"
                    - "9781475729412"
              access:
                class: record
      relations:
        - kind: part_of
          to: NWQC4TW7S9
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4615-6465-2
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4757-2941-2
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "3912289"
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
