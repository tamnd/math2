---
records:
    - id: THVSCV5X64
      kind: monograph
      title: Numerical Partial Differential Equations
      creators:
        - name: J. W. Thomas
          role: author
      date: "1995"
      msc:
        - code: 65M06
          from: zbmath_search
        - code: 62-02
          from: zbmath_search
        - code: 65M12
          from: zbmath_search
        - code: 35K15
          from: zbmath_search
        - code: 35L15
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1995"
          ids:
            doi:
                - 10.1007/978-1-4612-0569-2
                - 10.1007/978-1-4899-7278-1
            zbl: "0831.65087"
            zbl_id: "815352"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1999"
              ids:
                isbn:
                    - "9781461268215"
                    - "9781461205692"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1995"
              ids:
                isbn:
                    - "9781441931054"
                    - "9781489972781"
              access:
                class: record
      relations:
        - kind: part_of
          to: 7B8JKAVW9F
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-0569-2
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4899-7278-1
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "815352"
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
