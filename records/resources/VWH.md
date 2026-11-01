---
records:
    - id: VWHE18JRP8
      kind: monograph
      title: Complex Analysis
      creators:
        - name: Joseph Bak
          role: author
        - name: Donald J. Newman
          role: author
      date: "2010"
      msc:
        - code: 30-01
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2010"
          ids:
            doi: 10.1007/978-1-4419-7288-0
            zbl: "1205.30001"
            zbl_id: "5780980"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2010"
              ids:
                isbn:
                    - "9781441972873"
                    - "9781441972880"
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
          native_id: 10.1007/978-1-4419-7288-0
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "5780980"
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
