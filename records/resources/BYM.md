---
records:
    - id: BYMVJ6YPXF
      kind: monograph
      title: 'Reading, Writing, and Proving: A Closer Look at Mathematics'
      creators:
        - name: Ulrich Daepp
          role: author
        - name: Pamela Gorkin
          role: author
      date: "2011"
      msc:
        - code: 00A05
          from: zbmath_search
        - code: 03-01
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2011"
          ids:
            doi:
                - 10.1007/978-1-0716-4638-0
                - 10.1007/978-1-4419-9479-0
            zbl: "1230.00002"
            zbl_id: "5913333"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer US
              date: "2026"
              ids:
                isbn:
                    - "9781071646373"
                    - "9781071646380"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer New York
              date: "2011"
              ids:
                isbn:
                    - "9781441994783"
                    - "9781441994790"
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
          native_id: 10.1007/978-1-0716-4638-0
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4419-9479-0
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "5913333"
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
