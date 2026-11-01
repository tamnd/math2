---
records:
    - id: 2BXK1P7XW7
      kind: monograph
      title: A Practical Guide to Splines
      creators:
        - name: Carl de Boor
          role: author
      date: "1978"
      expressions:
        - key: e1
          kind: edition
          date: "1978"
          ids:
            doi: 10.1007/978-1-4612-6333-3
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1978"
              ids:
                isbn:
                    - "9780387903569"
                    - "9781461263333"
              access:
                class: record
      relations:
        - kind: part_of
          to: 2M0N86YNGA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-6333-3
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: 2BXNJQHGCT
      kind: monograph
      title: Semidynamical Systems in Infinite Dimensional Spaces
      creators:
        - name: Stephen H. Saperstone
          role: author
      date: "1981"
      msc:
        - code: 34-01
          from: zbmath_search
        - code: 60H10
          from: zbmath_search
        - code: 37C10
          from: zbmath_search
        - code: 34D20
          from: zbmath_search
        - code: 34C05
          from: zbmath_search
        - code: 45D05
          from: zbmath_search
        - code: 93C15
          from: zbmath_search
        - code: 93C20
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1981"
          ids:
            doi: 10.1007/978-1-4612-5977-0
            zbl: "0487.34044"
            zbl_id: "3766213"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1981"
              ids:
                isbn:
                    - "9780387906430"
                    - "9781461259770"
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
          native_id: 10.1007/978-1-4612-5977-0
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "3766213"
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
