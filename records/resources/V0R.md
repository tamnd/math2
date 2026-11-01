---
records:
    - id: V0R5E1VR15
      kind: monograph
      title: Probability Theory II
      creators:
        - name: Michel Loève
          role: author
      date: "1977"
      msc:
        - code: 60-01
          from: zbmath_search
        - code: 60Bxx
          from: zbmath_search
        - code: 60Gxx
          from: zbmath_search
        - code: 60Jxx
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          label: 4th edition
          language: en
          date: "1977"
          ids:
            doi:
                - 10.1007/978-1-4612-6257-2
                - 10.1007/978-1-4684-9464-8
                - 10.1007/978-1-4757-6288-4
            zbl: "0385.60001"
            zbl_id: "3599198"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1978"
              ids:
                isbn:
                    - "9780387943589"
                    - "9781461262572"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1977"
              ids:
                isbn:
                    - "9781468494662"
                    - "9781468494648"
              access:
                class: record
            - key: m3
              kind: print
              publisher: Springer New York
              date: "1977"
              ids:
                isbn:
                    - "9780387901275"
                    - "9781475762884"
              access:
                class: record
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-6257-2
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-9464-8
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4757-6288-4
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "3599198"
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
          by: m2 v0.6.14 scope/1
          note: from in to in
---
