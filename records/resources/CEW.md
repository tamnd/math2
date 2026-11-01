---
records:
    - id: CEWAJ1CB38
      kind: monograph
      title: Classical Fourier Analysis
      creators:
        - name: Loukas Grafakos
          role: author
      date: "2008"
      msc:
        - code: 42-01
          from: zbmath_search
        - code: 42Bxx
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2008"
          ids:
            doi:
                - 10.1007/978-0-387-09432-8
                - 10.1007/978-1-4939-1194-3
            zbl: "1220.42001"
            zbl_id: "5294798"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2008"
              ids:
                isbn:
                    - "9780387094311"
                    - "9780387094328"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer New York
              date: "2014"
              ids:
                isbn:
                    - "9781493911936"
                    - "9781493911943"
              access:
                class: record
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-0-387-09432-8
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4939-1194-3
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "5294798"
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
