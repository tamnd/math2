---
records:
    - id: BVTFXEKJ9Q
      kind: monograph
      title: Linear Algebra
      creators:
        - name: Larry Smith
          role: author
      date: "1978"
      msc:
        - code: 15-01
          from: zbmath_search
        - code: 15A03
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1978"
          ids:
            doi:
                - 10.1007/978-1-4612-1670-4
                - 10.1007/978-1-4615-9995-1
                - 10.1007/978-1-4684-0252-0
            zbl: "0374.15001"
            zbl_id: "3582302"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1998"
              ids:
                isbn:
                    - "9781461272380"
                    - "9781461216704"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer US
              date: "1978"
              ids:
                isbn:
                    - "9781461599975"
                    - "9781461599951"
              access:
                class: record
            - key: m3
              kind: print
              publisher: Springer US
              date: "1984"
              ids:
                isbn:
                    - "9781468402544"
                    - "9781468402520"
              access:
                class: record
      relations:
        - kind: part_of
          to: NWQC4TW7S9
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-1670-4
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4615-9995-1
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-0252-0
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "3582302"
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
