---
records:
    - id: VHZMPPYSTQ
      kind: monograph
      title: Mathematical Analysis I
      creators:
        - name: Vladimir A. Zorich
          role: author
      date: "2015"
      msc:
        - code: 00A05
          from: zbmath_search
        - code: 26-01
          from: zbmath_search
        - code: 26Axx
          from: zbmath_search
        - code: 26Bxx
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2015"
          ids:
            doi:
                - 10.1007/978-3-662-48792-1
                - 10.1007/978-3-662-48993-2
            zbl: "1332.00009"
            zbl_id: "6520144"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2015"
              ids:
                isbn:
                    - "9783662487907"
                    - "9783662487921"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2016"
              ids:
                isbn:
                    - "9783662489918"
                    - "9783662489932"
              access:
                class: record
      relations:
        - kind: part_of
          to: W0CC03QJC7
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-662-48792-1
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-662-48993-2
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "6520144"
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
