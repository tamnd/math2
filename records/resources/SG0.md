---
records:
    - id: SG0JJJJTWW
      kind: monograph
      title: 'Elementary Analysis: The Theory of Calculus'
      creators:
        - name: Kenneth A. Ross
          role: author
      date: "1980"
      msc:
        - code: 26-01
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1980"
          ids:
            doi:
                - 10.1007/978-1-4614-6271-2
                - 10.1007/978-1-4757-3971-8
            zbl: "0435.26001"
            zbl_id: "3678137"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2013"
              ids:
                isbn:
                    - "9781461462705"
                    - "9781461462712"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1980"
              ids:
                isbn:
                    - "9781441928115"
                    - "9781475739718"
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
          native_id: 10.1007/978-1-4614-6271-2
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4757-3971-8
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "3678137"
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
