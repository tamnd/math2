---
records:
    - id: TST01PDXSV
      kind: monograph
      title: Abstract Harmonic Analysis
      creators:
        - name: Edwin Hewitt
          role: author
        - name: Kenneth A. Ross
          role: author
      date: "1970"
      msc:
        - code: 43-02
          from: zbmath_search
        - code: 43A22
          from: zbmath_search
        - code: 43A05
          from: zbmath_search
        - code: 43A65
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1970"
          ids:
            doi:
                - 10.1007/978-1-4419-8638-2
                - 10.1007/978-3-642-62008-9
                - 10.1007/978-3-662-26755-4
            zbl: "0213.40103"
            zbl_id: "3338817"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1979"
              ids:
                isbn:
                    - "9780387941905"
                    - "9781441986382"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1970"
              ids:
                isbn:
                    - "9783540583189"
                    - "9783642620089"
              access:
                class: record
            - key: m3
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1970"
              ids:
                isbn:
                    - "9783662245958"
                    - "9783662267554"
              access:
                class: record
      relations:
        - kind: part_of
          to: GQFCNY816R
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4419-8638-2
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-642-62008-9
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-662-26755-4
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "3338817"
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
