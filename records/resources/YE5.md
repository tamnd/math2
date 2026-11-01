---
records:
    - id: YE55EGMKD4
      kind: monograph
      title: Mathematical Reflections
      creators:
        - name: Peter Hilton
          role: author
        - name: Derek Holton
          role: author
        - name: Jean Pedersen
          role: author
      date: "1997"
      msc:
        - code: 00-01
          from: zbmath_search
        - code: 00A35
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1997"
          ids:
            doi: 10.1007/978-1-4612-1932-3
            zbl: "0862.00001"
            zbl_id: "967953"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1997"
              ids:
                isbn:
                    - "9781461273455"
                    - "9781461219323"
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
          native_id: 10.1007/978-1-4612-1932-3
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "967953"
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
