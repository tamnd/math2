---
records:
    - id: M2R8VH10KB
      kind: monograph
      title: Unsolved Problems in Number Theory
      creators:
        - name: Richard K. Guy
          role: author
      date: "1994"
      msc:
        - code: 11-02
          from: zbmath_search
        - code: 00A07
          from: zbmath_search
        - code: 11Bxx
          from: zbmath_search
        - code: 11Dxx
          from: zbmath_search
        - code: 11Nxx
          from: zbmath_search
        - code: 11Pxx
          from: zbmath_search
        - code: 11Axx
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1994"
          ids:
            doi:
                - 10.1007/978-0-387-26677-0
                - 10.1007/978-1-4899-3585-4
            zbl: "0805.11001"
            zbl_id: "683826"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2004"
              ids:
                isbn:
                    - "9781441919281"
                    - "9780387266770"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1994"
              ids:
                isbn:
                    - "9781489935878"
                    - "9781489935854"
              access:
                class: record
      relations:
        - kind: part_of
          to: AQAR17SPHM
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-0-387-26677-0
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4899-3585-4
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "683826"
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
