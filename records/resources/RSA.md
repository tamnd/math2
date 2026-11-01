---
records:
    - id: RSAWP7FD23
      kind: monograph
      title: 'Mathematical Problems in Image Processing: Partial Differential Equations and the Calculus of Variations'
      creators:
        - name: Gilles Aubert
          role: author
        - name: Pierre Kornprobst
          role: author
      date: "2002"
      msc:
        - code: 35-02
          from: zbmath_search
        - code: 49-02
          from: zbmath_search
        - code: 68U05
          from: zbmath_search
        - code: 94A08
          from: zbmath_search
        - code: 35J20
          from: zbmath_search
        - code: 49J45
          from: zbmath_search
        - code: 49N99
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2002"
          ids:
            doi:
                - 10.1007/978-0-387-44588-5
                - 10.1007/b97428
            zbl: "1109.35002"
            zbl_id: "1703921"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2006"
              ids:
                isbn:
                    - "9780387322001"
                    - "9780387445885"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer New York
              date: "2002"
              ids:
                isbn:
                    - "9780387953267"
                    - "9780387217666"
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
          native_id: 10.1007/978-0-387-44588-5
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/b97428
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "1703921"
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
